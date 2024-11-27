import os
import csv
import time
import urllib.parse
import requests

def consulta(limite, pais, fechaInicio, fechaFinal, anomalia, ooni_run_link_id=None):
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
    for intento in range(reintentos):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            wait_time = 2 ** intento
            print(f"Error {response.status_code}, esperando {wait_time} segundos antes de intentar de nuevo...")
            time.sleep(wait_time)
    print("Error persistente después de reintentos.")
    return None


def filtrar_dns(datos):
    result = []
    if "results" in datos:
        for item in datos["results"]:
            if item.get("scores", {}).get("analysis", {}).get("blocking_type") == "dns":
                result.append(item)
    return result


def eliminar_duplicados(datos):
    seen_inputs = set()
    result = []
    
    for item in datos:
        input_value = item.get("input")
        if input_value not in seen_inputs:
            result.append(item)
            seen_inputs.add(input_value)
    
    return result


def guardar_en_csv(datos, archivo_salida, modo):
    if datos:
        with open(archivo_salida, mode=modo, newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=datos[0].keys())
            writer.writeheader()
            writer.writerows(datos)
        print(f"Datos guardados en {archivo_salida}")
    else:
        print("No hay datos para guardar.")


def obtenerDatosOONI(limite, pais, fechaInicio, fechaFinal, anomalia, ooni_run_link_id=None):
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
            guardar_en_csv(datos_sin_duplicados, f"Base_de_datos_OONI_por_ano\\{pais}.csv", "a")
        else:
            guardar_en_csv(datos_filtrados, f"Base_de_datos_actualiza\\{pais}-{ooni_run_link_id}.csv", "w")
            
        fechaInicio = fechaInicio + 1