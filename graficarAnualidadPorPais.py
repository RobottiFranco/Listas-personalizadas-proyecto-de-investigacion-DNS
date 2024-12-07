from Clases.Grafico import Grafico
from Clases.helper.globalVariables import category_code
from Clases.helper.globalVariables import consulta_grafica as base_url
from Clases.helper.obtenerDatosOoniDB import obtener_datos_ooni_db
from Clases.Consulta import Consulta


def graficar_anualidad_por_pais(probe_cc, ):
    consulta = Consulta(base_url, "web_connectivity", probe_cc, None, None, None, None, None, None, category_code)