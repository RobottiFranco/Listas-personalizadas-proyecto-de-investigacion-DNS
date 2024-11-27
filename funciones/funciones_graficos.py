import urllib.parse
import matplotlib.pyplot as plt

from .funciones_listas import *

def consulta_aggregacion(probe_cc, since, until, time_grain, axis_x, test_name, ooni_run_link_id=None):
    """ 
    Construye una URL para consultar la API de OONI con los parámetros especificado
    probe_cc: código de país
    since: fecha de inicio en formato "YYYY-MM-DD"
    until: fecha de final en formato "YYYY-MM-DD"
    time_grain: granularidad de tiempo
    axis_x: eje x
    test_name: nombre de la prueba
    ooni_run_link_id: identificador de las listas de OONI
    """
    base_url = "https://api.ooni.org/api/v1/aggregation?"
    
    parametros = {
        "probe_cc": probe_cc,
        "since": since,
        "until": until,
        "time_grain": time_grain,
        "axis_x": axis_x,
        "test_name": test_name,
    }
    
    if ooni_run_link_id is not None:
        parametros["ooni_run_link_id"] = ooni_run_link_id
    
    url = base_url + urllib.parse.urlencode(parametros)
    print(url)
    return url


def graficar(datos, probe_cc, ooni_run_link_id = None):
    """ 
    Genera un gráfico de barras a partir de los datos obtenidos de la API de OONI
    datos: datos en formato JSON obtenidos de la API de OONI por el metodo obtener_datos de la clase funciones_listas
    probe_cc: código de país
    ooni_run_link_id: identificador de las listas de OONI
    """
    datos = datos.get("result", [])
    
    categorias = [item["category_code"] for item in datos]
    anomalies = [item["anomaly_count"] for item in datos]

    plt.figure(figsize=(12, 6))
    plt.bar(categorias, anomalies, color='yellow')

    if ooni_run_link_id == None:
        plt.title(f"Conteo de anomalías por categoría para {probe_cc} OONI explorer", fontsize=16)
    else:
        plt.title(f"Conteo de anomalías por categoría para {probe_cc} OONI link: {ooni_run_link_id}", fontsize=16)
    plt.xlabel("Categorías", fontsize=14)
    plt.ylabel("Número de anomalías", fontsize=14)
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.show()


def generar_graficos(probe_cc, since, until, time_grain, axis_x, test_name, ooni_run_link_id = None):
    """ 
    obtiene los datos de la API de OONI y genera un gráfico, metodo principal, se llama desde main
    probe_cc: código de país
    since: fecha de inicio en formato "YYYY-MM-DD"
    until: fecha de final en formato "YYYY-MM-DD"
    time_grain: granularidad de tiempo
    axis_x: eje x
    test_name: nombre de la prueba
    ooni_run_link_id: identificador de las listas de OONI
    """
    print(f"Iniciando el proceso de {probe_cc}...")

    url = consulta_aggregacion(probe_cc, since, until, time_grain, axis_x, test_name, ooni_run_link_id)
    
    datos = obtener_datos(url, reintentos=3)
    
    if datos is None:
        print(f"No se pudieron obtener datos de {probe_cc}")
        return
    
    graficar(datos, probe_cc, ooni_run_link_id)