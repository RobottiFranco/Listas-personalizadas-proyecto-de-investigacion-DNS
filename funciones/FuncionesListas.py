import os
import csv
import time
import urllib.parse
import requests

def consulta(limit, probe_cc, since, until, anomaly, ooni_run_link_id=None):
    """
    Construye una URL para consultar la API de OONI con los parámetros especificados
    limit: número de resultados a obtener
    probe_cc: código de país
    since: fecha de inicio en formato "YYYY-MM-DD"
    until: fecha de final en formato "YYYY-MM-DD"
    anomaly: booleano para indicar si se quieren obtener resultados anómalos o no
    ooni_run_link_id: identificador de las listas de OONI
    """
    baseUrl= "https://api.ooni.org/api/v1/measurements?"
    parametros = {
        "limit": limit,
        "probe_cc": probe_cc,
        "test_name": "web_connectivity",
        "since": since,
        "until": until,
        "anomaly": anomaly
    }
    
    if ooni_run_link_id is not None:
        parametros["ooni_run_link_id"] = ooni_run_link_id
     
    url = baseUrl + urllib.parse.urlencode(parametros)
    print(url)
    return url


def obtener_datos(url, retries=3):
    """
    Realiza una solicitud GET a la URL especificada y devuelve los datos en formato JSON
    url: URL de la API de OONI
    retries: número de veces que se intentará obtener los datos en caso de error (sistema de backoff exponencial)
    """
    for intento in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            wait_time = 2 ** intento
            print(f"Error {e}, reintentando en {wait_time} segundos...")
            time.sleep(wait_time)
    print("Error persistente después de retries.")
    return None


def filtrar_dns(datos):
    """ 
    Filtra los datos obtenidos de la API de OONI para obtener solo los resultados de bloqueo por DNS
    datos: datos en formato JSON obtenidos de la API de OONI por el metodo obtener_datos
    """
    result = []
    if "results" in datos:
        for item in datos["results"]:
            if item.get("scores", {}).get("analysis", {}).get("blocking_type") == "dns":
                result.append(item)
    return result


def eliminar_duplicados(datos):
    """ 
    Elimina los datos duplicados de la lista de datos
    datos: lista de datos en formato JSON obtenidos de la API de OONI por el metodo filtrar_dns
    """
    seen_inputs = set()
    result = []
    
    for item in datos:
        input_value = item.get("input")
        if input_value not in seen_inputs:
            result.append(item)
            seen_inputs.add(input_value)
    
    return result


def guardar_en_csv(datos, archivo_salida, modo):
    """
    Guarda los datos en un archivo CSV
    datos: lista de datos en formato JSON obtenidos de la API de OONI por el metodo eliminar_duplicados
    archivo_salida: nombre del archivo CSV donde se guardarán los datos
    modo: modo de apertura del archivo ("w" para sobreescribir, "a" para añadir)
    """
    if datos:
        with open(archivo_salida, mode=modo, newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=datos[0].keys())
            writer.writeheader()
            writer.writerows(datos)
        print(f"Datos guardados en {archivo_salida}")
    else:
        print("No hay datos para guardar.")


def obtenerDatosOONI(limit, probe_cc, since, until, anomaly, ooni_run_link_id=None):
    """
    Obtiene los datos de la API de OONI, los filtra y los guarda en un archivo CSV, metodo principal, se ejecuta en el main.
    limit: número de resultados a obtener
    probe_cc: código de país
    since: año de inicio
    until: año de final
    anomaly: booleano para indicar si se quieren obtener resultados anómalos o no
    ooni_run_link_id: identificador de las listas de OONI
    """
    while since <= until:
        inicio = f"{since}-01-01"
        final = f"{since}-12-31"
        print(f"Iniciando el proceso de {probe_cc}...")
        
        url = consulta(limit, probe_cc, inicio, final, anomaly, ooni_run_link_id)
        datos = obtener_datos(url)
        if datos is None:
            print(f"No se pudieron obtener datos de {probe_cc}")
            return
        datos_filtrados = filtrar_dns(datos)
        datos_sin_duplicados = eliminar_duplicados(datos_filtrados)
        if ooni_run_link_id is None:
            os.makedirs("Base_de_datos_OONI_por_ano", exist_ok=True)
            guardar_en_csv(datos_sin_duplicados, f"Base_de_datos_OONI_por_ano\\{probe_cc}.csv", "a")
        else:
            os.makedirs("Base_de_datos_actualizada", exist_ok=True)
            guardar_en_csv(datos_sin_duplicados, f"Base_de_datos_actualizada\\{probe_cc}-{ooni_run_link_id}.csv", "w")
            
        since = since + 1