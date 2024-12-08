from Clases.Consulta import Consulta
from Clases.helper.obtenerDatosOoniDB import obtener_datos_ooni_db
from Clases.helper.globalVariables import diccionario_Paise_lista_ooni_historica, consulta_db as base_url
from Clases.CSVHandler import CSVHandler
from Clases.helper.calcularRangoFechaMes import obtener_rango_mes

def extraer_datos_por_mes(since: int, until: int) -> None:
    for pais in diccionario_Paise_lista_ooni_historica:
        while since <= until:
            for month in range(1, 13):
                inicio, final = obtener_rango_mes(since, month)
                consulta = Consulta(base_url, "web_connectivity", pais, inicio, final, None, None, None, None, None)
                obtener_datos_ooni_db(consulta, 2000, "true", "Base_de_datos/historica", pais, "a")
            since += 1


def crear_ooni_run_link_historica() -> None:    
    for pais in diccionario_Paise_lista_ooni_historica:
        CSVHandler().crear_ooni_run_link(f"Base_de_datos/historica/{pais}.csv", f"{pais}_HISTORICA", "Listas_OONI/historicas")


# Main

extraer_datos_por_mes(since=2016, until=2024)
crear_ooni_run_link_historica()