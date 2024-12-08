from Clases.Grafico import Grafico
from Clases.helper.calcularRangoFechaMes import obtener_rango_mes
from Clases.helper.globalVariables import consulta_grafica as base_url, diccionario_Paise_lista_ooni_historica
from Clases.helper.obtenerDatosOoniDB import obtener_datos_ooni_db
from Clases.Consulta import Consulta
from Clases.helper.obtenerGrafico import obtener_grafico


def graficar_anualidad_por_pais(since: int, until: int) -> None:
    for pais in diccionario_Paise_lista_ooni_historica:
        while since <= until:
            consulta = Consulta(base_url, "web_connectivity", pais, f"{since}-01-01", f"{since}-12-31", None, None, None, None, None)
            obtener_grafico(consulta, "month", "category_code", None, f"Graficos/anuales/{pais}", since)
            since += 1
        since = 2016

# Main

graficar_anualidad_por_pais(2016, 2024)