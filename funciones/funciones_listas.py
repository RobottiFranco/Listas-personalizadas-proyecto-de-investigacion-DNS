import os
import csv
import time
import urllib.parse
import requests

def consulta(limite, pais, fechaInicio, fechaFinal, anomalia, ooni_run_link_id=None):
    """
    Construye una URL para consultar la API de OONI con los parámetros especificados
    limite: número de resultados a obtener
    pais: código de país
    fechaInicio: fecha de inicio en formato "YYYY-MM-DD"
    fechaFinal: fecha de final en formato "YYYY-MM-DD"
    anomalia: booleano para indicar si se quieren obtener resultados anómalos o no
    ooni_run_link_id: identificador de las listas de OONI
    """
    baseUrl= "https://api.ooni.org/api/v1/measurements?"
    parametros = {
        "limit": limite,
        "probe_cc": pais,
        "test_name": "web_connectivity",
        "since": fechaInicio,
        "until": fechaFinal,
        "anomaly": anomalia
    }
    
    if ooni_run_link_id is not None:
        parametros["ooni_run_link_id"] = ooni_run_link_id
     
    url = baseUrl + urllib.parse.urlencode(parametros)
    print(url)
    return url


def obtener_datos(url, reintentos=3):
    """
    Realiza una solicitud GET a la URL especificada y devuelve los datos en formato JSON
    url: URL de la API de OONI
    reintentos: número de veces que se intentará obtener los datos en caso de error (sistema de backoff exponencial)
    """
    for intento in range(reintentos):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            wait_time = 2 ** intento
            print(f"Error {e}, reintentando en {wait_time} segundos...")
            time.sleep(wait_time)
    print("Error persistente después de reintentos.")
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


def obtenerDatosOONI(limite, pais, fechaInicio, fechaFinal, anomalia, ooni_run_link_id=None):
    """
    Obtiene los datos de la API de OONI, los filtra y los guarda en un archivo CSV, metodo principal, se ejecuta en el main.
    limite: número de resultados a obtener
    pais: código de país
    fechaInicio: año de inicio
    fechaFinal: año de final
    anomalia: booleano para indicar si se quieren obtener resultados anómalos o no
    ooni_run_link_id: identificador de las listas de OONI
    """
    while fechaInicio <= fechaFinal:
        inicio = f"{fechaInicio}-01-01"
        final = f"{fechaInicio}-12-31"
        print(f"Iniciando el proceso de {pais}...")
        
        url = consulta(limite, pais, inicio, final, anomalia, ooni_run_link_id)
        datos = obtener_datos(url)
        if datos is None:
            print(f"No se pudieron obtener datos de {pais}")
            return
        datos_filtrados = filtrar_dns(datos)
        if ooni_run_link_id is None:
            datos_sin_duplicados = eliminar_duplicados(datos_filtrados)
            os.makedirs("Base_de_datos_OONI_por_ano", exist_ok=True)
            guardar_en_csv(datos_sin_duplicados, f"Base_de_datos_OONI_por_ano\\{pais}.csv", "a")
        else:
            os.makedirs("Base_de_datos_actualizada", exist_ok=True)
            guardar_en_csv(datos_filtrados, f"Base_de_datos_actualizada\\{pais}-{ooni_run_link_id}.csv", "w")
            
        fechaInicio = fechaInicio + 1