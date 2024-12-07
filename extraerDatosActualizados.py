from Clases.helper.globalVariables import diccionario_Paise_lista_ooni_historica, consulta_db as base_url
from Clases.Consulta import Consulta
from Clases.helper.obtenerDatosOoniDB import obtener_datos_ooni_db
from Clases.CSVHandler import CSVHandler

def extraer_datos_actualizados():
    for pais in diccionario_Paise_lista_ooni_historica:
        inicio = "2024-09-01"
        final = "2025-06-28"
        consulta = Consulta(base_url, "web_connectivity", pais, inicio, final, diccionario_Paise_lista_ooni_historica[pais], None, None, None, None)
        obtener_datos_ooni_db(consulta, 2000, "true", "Base_de_datos_OONI_actualizada", pais, "w")
        

extraer_datos_actualizados()
CSVHandler().crear_ooni_run_link("Base_de_datos_OONI_por_ano", {pais: pais for pais in diccionario_Paise_lista_ooni_historica}, "Listas_de_OONI_actualizada")