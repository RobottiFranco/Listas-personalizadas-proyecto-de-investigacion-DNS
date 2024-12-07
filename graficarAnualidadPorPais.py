from Clases.Grafico import Grafico
from Clases.helper.calcularRangoFechaMes import obtener_rango_mes
from Clases.helper.globalVariables import consulta_grafica as base_url
from Clases.helper.obtenerDatosOoniDB import obtener_datos_ooni_db
from Clases.Consulta import Consulta
from Clases.helper.obtenerGrafico import obtener_grafico


def graficar_anualidad_por_pais(probe_cc: str, since: int, until: int) -> None:
    while since <= until:
        for month in range(1, 13):
            inicio, final = obtener_rango_mes(since, month)
            consulta = Consulta(base_url, "web_connectivity", probe_cc, inicio, final, None, None, None, None, None)
            obtener_grafico(consulta, "month", "category_code", None, f"graficos_anuales_{probe_cc}", f"{probe_cc} {since}")       
            month += 1
        since += 1