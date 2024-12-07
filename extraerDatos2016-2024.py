from Clases.Consulta import Consulta
from Clases.helper.obtenerDatosOoniDB import obtener_datos_ooni_db
from Clases.helper.globalVariables import diccionario_Paise_lista_ooni_historica, consulta_db as base_url
from Clases.CSVHandler import CSVHandler
from Clases.helper.calcularRangoFechaMes import obtener_rango_mes

def extraer_datos(since, until):
    for pais in diccionario_Paise_lista_ooni_historica:
        while since <= until:
            for month in range(1, 13):
                inicio, final = obtener_rango_mes(since, month)
                consulta = Consulta(base_url, "web_connectivity", pais, inicio, final, None, None, None, None, None)
                obtener_datos_ooni_db(consulta, 2000, "true", "Base_de_datos_OONI_por_ano", pais, "a")
            since += 1

extraer_datos(since=2016, until=2024)

CSVHandler().crear_ooni_run_link("Base_de_datos_OONI_por_ano", {pais: pais for pais in diccionario_Paise_lista_ooni_historica}, "Listas_de_OONI_historicas")