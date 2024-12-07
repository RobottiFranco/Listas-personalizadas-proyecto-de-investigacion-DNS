import os
from Clases.helper.calcularRangoFechaMes import obtener_rango_mes
from Clases.Consulta import Consulta
from Clases.helper.globalVariables import category_code
from Clases.helper.globalVariables import consulta_db as base_url
from Clases.helper.obtenerDatosOoniDB import obtener_datos_ooni_db


def obtener_metricas_por_categoria_y_ano(since: int, until: int, probe_cc: str) -> None:
    for category in category_code:
        while since <= until:
            for month in range(1, 13):
                inicio, final = obtener_rango_mes(since, month)
                consulta = Consulta(base_url, "web_connectivity", probe_cc, inicio, final, None, None, None, None, category)
                obtener_datos_ooni_db(consulta, 2000, "true", "graficos_por_ano", probe_cc, "w")                
                month += 1
            since += 1
            
