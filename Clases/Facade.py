import os

from .Consulta import *
from .ClienteAPI import *
from .CSVHandler import *
from .Grafico import *

diccionarioPaises_ooni_historica = {"UY": "10091", "VE": "10092", "HN": "10093", "AR": "10094", "CU": "10095", "SV": "10096", "NI": "10097", "GT": "10098"}
diccionarioPaises_ooni_actualizada = {"UY": "10100"}

def obtenerDatosOONI(limit, probe_cc, since, until, anomaly, ooni_run_link_id=None):
    url = Consulta(probe_cc, since, until, ooni_run_link_id)
    url = url.armar_consulta_db_OONI(limit, anomaly, "web_connectivity")
    print(url)
    
    datos = ClienteAPI(url, 3)
    datos = datos.realizar_solicitud_obtencion()
    if datos is None:
        print(f"No se pudieron obtener datos de {probe_cc} desde {since} hasta {until}")
        return
    
    csv = CSVHandler()
    datosFiltrados = csv.filtrar_dns(datos)
    datos_sin_duplicados = csv.eliminar_duplicados(datosFiltrados)       
    
    if ooni_run_link_id is None:
        os.makedirs("Base_de_datos_OONI_por_ano", exist_ok=True)
        csv.guardar_en_csv(f"Base_de_datos_OONI_por_ano\\{probe_cc}.csv", datos_sin_duplicados, "a")
    else:
        os.makedirs("Base_de_datos_actualizada", exist_ok=True)
        csv.guardar_en_csv(f"Base_de_datos_actualizada\\{probe_cc}-{ooni_run_link_id}.csv", datos_sin_duplicados, "w")
        
        
def generar_graficos(probe_cc, since, until, time_grain, axis_x, test_name, ooni_run_link_id = None):
    print(f"Iniciando el proceso grafico de {probe_cc}...")
    
    url = Consulta(probe_cc, since, until, ooni_run_link_id)
    url = url.armar_consulta_grafica(time_grain, axis_x, test_name)
    
    datos = ClienteAPI(url, 3)
    datos = datos.realizar_solicitud_obtencion() 
       
    if datos is None:
        print(f"No se pudieron obtener datos de {probe_cc}")
        return
    
    grafico = Grafico(datos, probe_cc, ooni_run_link_id)
    grafico.graficarBarrasAnomalias()

def extraer_datos():
    for pais in diccionarioPaises_ooni_historica:
        since = 2016
        until = 2024
        while since <= until:
            month = 1
            while month <= 12:
                inicio = f"{since}-{month:02d}-01"
                if month == 2:
                    final = f"{since}-{month:02d}-28"
                elif month in [4, 6, 9, 11]:
                    final = f"{since}-{month:02d}-30"
                else:
                    final = f"{since}-{month:02d}-31"
                obtenerDatosOONI(2000, pais, inicio, final, "true")
                month += 1
            since += 1
            
def extraer_datos_listaHistorica():
    for pais in diccionarioPaises_ooni_historica:
        since = 2016
        until = 2024
        while since <= until:
            month = 1
            while month <= 12:
                inicio = f"{since}-{month:02d}-01"
                if month == 2:
                    final = f"{since}-{month:02d}-28"
                elif month in [4, 6, 9, 11]:
                    final = f"{since}-{month:02d}-30"
                else:
                    final = f"{since}-{month:02d}-31"
                obtenerDatosOONI(2000, pais, inicio, final, "true", diccionarioPaises_ooni_historica[pais])
                month += 1
            since += 1
    
def crearOnniRunLink():
    os.makedirs("Listas_de_OONI_historicas", exist_ok=True)
    for pais in diccionarioPaises_ooni_historica:
        csv = CSVHandler()
        csv.compenetrar_csv(f"Base_de_datos_OONI_por_ano\\{pais}.csv", f"Listas_de_OONI_historicas\\{pais}_HISTORICA.csv")

def crearOnniRunLink_partiendo_de_historica():
    os.makedirs("Listas_de_OONI_actualizada", exist_ok=True)
    for pais in diccionarioPaises_ooni_historica:
        csv = CSVHandler()
        csv.compenetrar_csv(f"Base_de_datos_actualizada\\{pais}-{diccionarioPaises_ooni_historica[pais]}.csv", f"Listas_de_OONI_actualizada\\{pais}_ACTUALIZADA.csv")


def graficar():
    for pais in diccionarioPaises_ooni_actualizada:
        generar_graficos(pais, "2016-01-01", "2024-12-31", "month", "category_code", "web_connectivity")
        generar_graficos(pais, "2024-01-01", "2024-12-31", "month", "category_code", "web_connectivity", diccionarioPaises_ooni_historica[pais])
        generar_graficos(pais, "2024-01-01", "2024-12-31", "month", "category_code", "web_connectivity", diccionarioPaises_ooni_actualizada[pais])
        