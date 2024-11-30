import os
from Clases.Facade import *

diccionarioPaises_ooni_historica = {"UY": "10081"}
diccionarioPaises_ooni_actualizada = {"UY": "10089"}

def iniciarExtraccio():
    # 1- CREACION LISTA HISTORICA DE CADA PAIS
    """ 
        Se obtienen los datos de OONI de cada pais desde 2016 hasta 2024, en cada mes de cada año se toman 2000 datos.
        Se guardan en la carpeta "Listas_de_OONI_historicas"
    """
    os.makedirs("Listas_de_OONI_historicas", exist_ok=True)
    for pais in diccionarioPaises_ooni_historica:
        since = 2016
        until = 2024
        while since <= until:
            month = 1
            while month <= 12:
                inicio = f"{since}-{month:02d}-01"
                final = f"{since}-{month:02d}-31"
                exito = obtenerDatosOONI(2000, pais, inicio, final, "true")
                if not exito:
                    print(f"Fallo en {pais}, {inicio} a {final}. Continuando...")
                    break
                month += 1
            since += 1
                

# 2- CREACION LISTA ACTUALIZADA DE CADA PAIS

os.makedirs("Listas_de_OONI_actualizada", exist_ok=True)
""" 
for pais in diccionarioPaises_ooni_historica:
    obtenerDatosOONI(2000, pais, 2024, 2024, "true", diccionarioPaises_ooni_historica[pais])
    crearOnniRunLink(f"Base_de_datos_actualizada\\{pais}-{diccionarioPaises_ooni_historica['UY']}.csv", f"Listas_de_OONI_actualizada\\{pais}_ACTUALIZADA.csv")
 """
# 3-GRAFICAR LISTAS OONI HISOTRICAS Y ACTUALIZADAS
def graficar():
    for pais in diccionarioPaises_ooni_actualizada:
        generar_graficos(pais, "2016-01-01", "2024-12-31", "month", "category_code", "web_connectivity")
        generar_graficos(pais, "2024-01-01", "2024-12-31", "month", "category_code", "web_connectivity", diccionarioPaises_ooni_historica[pais])
        generar_graficos(pais, "2024-01-01", "2024-12-31", "month", "category_code", "web_connectivity", diccionarioPaises_ooni_actualizada[pais])
        
iniciarExtraccio()