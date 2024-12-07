from Clases.helper.obtenerGrafico import obtener_grafico
from Clases.helper.globalVariables import diccionario_Pais_lista_ooni_actualizada, diccionario_Paise_lista_ooni_historica, consulta_grafica as base_url
from Clases.Consulta import Consulta

def graficar_pais():
    for pais in diccionario_Pais_lista_ooni_actualizada:
        consulta = Consulta(base_url, "web_connectivity", pais, "2016-01-01", "2024-12-31", None, None, None, None)
        obtener_grafico(consulta, "month", "category_code", None, "graficos_paises", f"{pais} OONI Explorer")
                
        consulta = Consulta(base_url, "web_connectivity", pais, "2016-01-01", "2024-12-31", diccionario_Paise_lista_ooni_historica[pais], None, None, None, None)
        obtener_grafico(consulta, "month", "category_code", None, "graficos_paises", f"{pais} actualizada sin VPN")
        
        consulta = Consulta(base_url, "web_connectivity", pais, "2016-01-01", "2024-12-31", diccionario_Pais_lista_ooni_actualizada[pais], None, None, None, None)
        obtener_grafico(consulta, "month", "category_code", None, "graficos_paises", f"{pais} actualizada sin VPN")

