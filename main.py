import os
from Funciones.FuncionesCSV import crearOnniRunLink
from Funciones.FuncionesListas import obtenerDatosOONI
from Funciones.FuncionesGraficos import generar_graficos

diccionarioPaises_ooni_historica = {"UY": "10081", "VE": "10082", "HN": "10083", "AR": "10084", "CU": "10085", "SV": "10086", "NI": "10087", "GT": "10088"}
diccionarioPaises_ooni_actualizada = {"UY": "10089"}

# 1- OBTENER DATOS DE OONI, SE TOMAN 2000 POR AÑO DE CADA PAIS y PREPARACION DE LISTAS HISTORIAS DE CADA PAIS
# 2000 ES EL LIMITE EN CASO DE QUE HAYA MENOS SE TOMA MENOS
# este primer metodo no es idempotente, se ejecuta una sola vez para obtener las listas historicas de cada pais
"""
os.makedirs("Listas_de_OONI_historicas", exist_ok=True)
for pais in diccionarioPaises_ooni_historica:
    obtenerDatosOONI(2000, pais, 2016, 2024, "true")
    crearOnniRunLink(f"Base_de_datos_OONI_por_ano\\{pais}.csv", f"Listas_de_OONI_historicas\\{pais}_HISTORICA.csv")
""" 
# 2- CREACION LISTA ACTUALIZADA DE CADA PAIS

os.makedirs("Listas_de_OONI_actualizada", exist_ok=True)
for pais in diccionarioPaises_ooni_historica:
    obtenerDatosOONI(2000, pais, 2024, 2024, "true", diccionarioPaises_ooni_historica[pais])
    crearOnniRunLink(f"Base_de_datos_actualizada\\{pais}-{diccionarioPaises_ooni_historica['UY']}.csv", f"Listas_de_OONI_actualizada\\{pais}_ACTUALIZADA.csv")

# 3-GRAFICAR LISTAS OONI HISOTRICAS Y ACTUALIZADAS

for pais in diccionarioPaises_ooni_historica:
    # historico de ooni explorer
    generar_graficos(probe_cc=pais, since="2016-01-01", until="2024-12-31", time_grain="month", axis_x="category_code", test_name="web_connectivity")
    # historico (actual) de ooni link (bloqueos de dns, ip, etc)
    generar_graficos(probe_cc=pais, since="2016-01-01", until="2024-12-31", time_grain="month", axis_x="category_code", test_name="web_connectivity", ooni_run_link_id=diccionarioPaises_ooni_historica[pais])
    # actualizado de ooni link (bloqueos de dns only)
    generar_graficos(probe_cc=pais, since="2016-01-01", until="2024-12-31", time_grain="month", axis_x="category_code", test_name="web_connectivity", ooni_run_link_id=diccionarioPaises_ooni_actualizada[pais])