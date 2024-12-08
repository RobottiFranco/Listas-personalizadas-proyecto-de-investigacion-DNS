from Clases.Grafico import Grafico
from Clases.helper.calcularRangoFechaMes import obtener_rango_mes
from Clases.helper.globalVariables import consulta_grafica as base_url, diccionario_Paise_lista_ooni_historica
from Clases.helper.obtenerDatosOoniDB import obtener_datos_ooni_db
from Clases.Consulta import Consulta
from Clases.helper.obtenerGrafico import obtener_grafico, obtener_grafico_mejorado


def graficar_anualidad_por_pais(since: int, until: int, mejorado: bool = False) -> None:
    for pais in diccionario_Paise_lista_ooni_historica:
        init = since
        while since <= until:
            consulta = Consulta(base_url, "web_connectivity", pais, f"{init}-01-01", f"{since}-12-31", None, None, None, None, None)
            if mejorado:
                obtener_grafico_mejorado(consulta, "month", "category_code", None, f"Graficos/anuales/mejorados/{pais}", since)
            else:
                obtener_grafico(consulta, "month", "category_code", None, f"Graficos/anuales/nativos/{pais}", since)
            since += 1
        since = 2016

# Main

graficar_anualidad_por_pais(2016, 2024)
graficar_anualidad_por_pais(2016, 2024, True)