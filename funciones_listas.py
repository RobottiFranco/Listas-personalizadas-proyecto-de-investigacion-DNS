import os
import csv
import time
import urllib.parse
import requests

def consulta(limite, pais, fechaInicio, fechaFinal, anomalia):
    baseUrl= "https://api.ooni.org/api/v1/measurements?"
    parametros = {
        "limit": limite,
        "probe_cc": pais,
        "test_name": "web_connectivity",
        "since": fechaInicio,
        "until": fechaFinal,
        "anomaly": anomalia
    }
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


def guardar_en_csv(datos, archivo_salida):
    if datos:
        with open(archivo_salida, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=datos[0].keys())
            writer.writeheader()
            writer.writerows(datos)
        print(f"Datos guardados en {archivo_salida}")
    else:
        print("No hay datos para guardar.")


def obtenerDatos(limite, pais, fechaInicio, fechaFinal, anomalia):
    print(f"Iniciando el proceso de {pais}...")
    
    # Paso 1: Armar consulta
    url = consulta(limite, pais, fechaInicio, fechaFinal, anomalia)
    
    # Paso 2: Obtener los datos de la API
    datos = obtener_datos(url)
    
    if datos is None:
        print(f"No se pudieron obtener datos de {pais}")
        return

    # Paso 3: Filtrar los resultados por 'blocking_type': 'dns'
    datos_filtrados = filtrar_dns(datos)
    
    # Paso 4: Eliminar los duplicados basados en 'input'
    datos_sin_duplicados = eliminar_duplicados(datos_filtrados)
    
    # Paso 5: Guardar los resultados en un archivo CSV
    guardar_en_csv(datos_sin_duplicados, f"resultados\\{pais}.csv")
    