from Clases.helper.globalVariables import diccionario_Paise_lista_ooni_historica, consulta_db as base_url
from Clases.Consulta import Consulta
from Clases.helper.obtenerDatosOoniDB import obtener_datos_ooni_db
from Clases.CSVHandler import CSVHandler

def extraer_datos_actualizados(since: str, until: str) -> None:
    for pais in diccionario_Paise_lista_ooni_historica:
        consulta = Consulta(base_url, "web_connectivity", pais, since, until, diccionario_Paise_lista_ooni_historica[pais], None, None, None, None)
        obtener_datos_ooni_db(consulta, 2000, "true", "Base_de_datos/actualizada", pais, "w")
        

extraer_datos_actualizados("2024-09-01", "2025-06-28")

CSVHandler().crear_ooni_run_link("Base_de_datos/actualizada", {pais: pais for pais in diccionario_Paise_lista_ooni_historica}, "Listas_OONI/actualizada")