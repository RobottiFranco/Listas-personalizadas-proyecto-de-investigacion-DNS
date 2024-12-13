import csv
from Clases.helper.globalVariables import diccionario_Paise_lista_ooni_historica, consulta_db as base_url, category_code
from Clases.Consulta import Consulta
from Clases.helper.obtenerDatosOoniDB import obtener_datos_ooni_db_actualizados
from Clases.CSVHandler import CSVHandler

def extraer_datos_actualizados(since: str, until: str, ooni_run_link_id: str, pais: str, asn: str = None) -> None:
    for category in category_code:
        consulta = Consulta(base_url, "web_connectivity", pais, since, until, ooni_run_link_id, asn, None, None, category)
        
        nombre_archivo = nombre(pais, asn)
        obtener_datos_ooni_db_actualizados(consulta, 2000, "true", "Base_de_datos/actualizada", f"{nombre_archivo} prueba", "a")

def crear_ooni_run_link_actualizado(nombre_entrada: str, pais: str, asn: str = None) -> None:
    nombre_archivo = nombre(pais, asn)
    CSVHandler().crear_ooni_run_link(f"Base_de_datos/actualizada/{nombre_entrada}_prueba.csv", nombre_archivo, "Listas_OONI/actualizada")

def nombre(pais: str, asn: str) -> str:
    if asn:
        return f"{pais}_{asn}"
    else:
        return f"{pais}"
    
# Main

for pais in diccionario_Paise_lista_ooni_historica:
    if pais == "AR":
        extraer_datos_actualizados("2024-11-08", "2025-06-28", diccionario_Paise_lista_ooni_historica[pais], pais, "AS16814")
        extraer_datos_actualizados("2024-11-08", "2025-06-28", diccionario_Paise_lista_ooni_historica[pais], pais, "AS7303")
        
        crear_ooni_run_link_actualizado(f"{pais}_AS16814", pais, "AS16814")
        crear_ooni_run_link_actualizado(f"{pais}_AS7303", pais, "AS7303")
    else:
        extraer_datos_actualizados("2024-11-08", "2025-06-28", diccionario_Paise_lista_ooni_historica[pais], pais, None)

        crear_ooni_run_link_actualizado(pais, pais)
