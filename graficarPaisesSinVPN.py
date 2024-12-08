from Clases.helper.obtenerGrafico import obtener_grafico
from Clases.helper.globalVariables import diccionario_Pais_lista_ooni_actualizada, diccionario_Paise_lista_ooni_historica, consulta_grafica as base_url
from Clases.Consulta import Consulta

def graficar_lista_historica_sin_VPN():
    for pais in diccionario_Pais_lista_ooni_actualizada:
        consulta = Consulta(base_url, "web_connectivity", pais, "2024-01-01", "2025-12-31", diccionario_Paise_lista_ooni_historica[pais], None, None, None, None, None)
        obtener_grafico(consulta, "month", "category_code", None, "Graficos/historico_sin_vpn", f"{pais} historica sin VPN (todo tipo de bloqueos)")
        
def graficar_lista_actualizada_sin_VPN():
    for pais in diccionario_Pais_lista_ooni_actualizada:
        consulta = Consulta(base_url, "web_connectivity", pais, "2024-01-01", "2025-12-31", diccionario_Pais_lista_ooni_actualizada[pais], None, None, None, None, None)
        obtener_grafico(consulta, "month", "category_code", None, "Graficos/actualizado_sin_vpn", f"{pais} actualizada sin VPN (solo DNS)")

def graficar_OONI_explorer():
    for pais in diccionario_Paise_lista_ooni_historica:
        consulta = Consulta(base_url, "web_connectivity", pais, "2016-01-01", "2024-12-31", None, None, None, None, None)
        obtener_grafico(consulta, "month", "category_code", None, "Graficos/ooni_explorer", f"{pais} OONI Explorer (todo tipo de bloqueos)")


# Main

graficar_OONI_explorer()

graficar_lista_historica_sin_VPN()

graficar_lista_actualizada_sin_VPN()



