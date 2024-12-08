from Clases.helper.obtenerGrafico import obtener_grafico, obtener_grafico_mejorado
from Clases.helper.globalVariables import diccionario_Pais_lista_ooni_actualizada, diccionario_Paise_lista_ooni_historica, consulta_grafica as base_url
from Clases.Consulta import Consulta

def graficar_OONI_explorer(mejorada: bool = False):
    for pais in diccionario_Paise_lista_ooni_historica:
        consulta = Consulta(base_url, "web_connectivity", pais, "2016-01-01", "2024-12-31", None, None, None, None, None)
        if mejorada:
            obtener_grafico_mejorado(consulta, "month", "category_code", None, "Graficos/listas/mejorados/ooni_explorer", f"{pais} OONI Explorer (todo tipo de bloqueos)")
        else:
            obtener_grafico(consulta, "month", "category_code", None, "Graficos/listas/nativos/ooni_explorer", f"{pais} OONI Explorer (todo tipo de bloqueos)")


def graficar_lista_historica(mejorada: bool = False):
    for pais in diccionario_Pais_lista_ooni_actualizada:
        consulta = Consulta(base_url, "web_connectivity", pais, "2024-01-01", "2025-12-31", diccionario_Paise_lista_ooni_historica[pais], None, None, None, None)
        if mejorada:
            obtener_grafico_mejorado(consulta, "month", "category_code", None, "Graficos/listas/mejorados/historico", f"{pais} historica sin VPN (todo tipo de bloqueos)")
        else:
            obtener_grafico(consulta, "month", "category_code", None, "Graficos/listas/nativos/historico", f"{pais} historica sin VPN (todo tipo de bloqueos)")

   
        
def graficar_lista_actualizada(mejorada: bool = False):
    for pais in diccionario_Pais_lista_ooni_actualizada:
        consulta = Consulta(base_url, "web_connectivity", pais, "2024-01-01", "2025-12-31", diccionario_Pais_lista_ooni_actualizada[pais], None, None, None, None)
        if mejorada:
            obtener_grafico_mejorado(consulta, "month", "category_code", None, "Graficos/listas/mejorados/actualizado", f"{pais} actualizada sin VPN (solo DNS)")
        else:
            obtener_grafico(consulta, "month", "category_code", None, "Graficos/listas/nativos/actualizado", f"{pais} actualizada sin VPN (solo DNS)")


# Main

graficar_OONI_explorer()
graficar_lista_historica()
graficar_lista_actualizada()

graficar_OONI_explorer(True)
graficar_lista_historica(True)
graficar_lista_actualizada(True)
