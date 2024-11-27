from funciones.funciones_csv import crearOnniRunLink
from funciones.funciones_listas import obtenerDatosOONI
from funciones.funciones_graficos import generar_graficos

diccionarioPaises_ooni_historica = {"UY": "10081", "VE": "10082", "HN": "10083", "AR": "10084", "CU": "10085", "SV": "10086", "NI": "10087", "GT": "10088"}
diccionarioPaises_ooni_actualizada = {"UY": "Uruguay"}

# 1- OBTENER DATOS DE OONI, SE TOMAN 2000 POR AÑO DE CADA PAIS y PREPARACION DE LISTAS HISTORIAS DE CADA PAIS
# 2000 ES EL LIMITE EN CASO DE QUE HAYA MENOS SE TOMA MENOS

""" 
for pais in diccionarioPaises_ooni_historica:
    obtenerDatosOONI(2000, pais, 2016, 2024, "true")
    crearOnniRunLink(f"Base_de_datos_OONI_por_ano\\{pais}.csv", f"Listas_de_OONI_historicas\\{pais}_HISTORICA.csv")
""" 
# 2- CREACION LISTA ACTUALIZADA DE CADA PAIS

for pais in diccionarioPaises_ooni_historica:
    obtenerDatosOONI(2000, pais, 2024, 2024, "true", diccionarioPaises_ooni_historica[pais])
    crearOnniRunLink(f"Base_de_datos_actualiza\\{pais}-OONI_RUN_LINK.csv", f"Listas_de_OONI_actualizadas\\{pais}_ACTUALIZADA.csv")

# 3-GRAFICAR LISTAS OONI HISOTRICAS Y ACTUALIZADAS

for pais in diccionarioPaises_ooni_historica:
    generar_graficos(probe_cc=pais, since="2016-01-01", until="2024-12-31", time_grain="month", axis_x="category_code", test_name="web_connectivity")
    generar_graficos(probe_cc=pais, since="2016-01-01", until="2024-12-31", time_grain="month", axis_x="category_code", test_name="web_connectivity", ooni_run_link_id=diccionarioPaises_ooni_historica[pais])
    generar_graficos(probe_cc=pais, since="2016-01-01", until="2024-12-31", time_grain="month", axis_x="category_code", test_name="web_connectivity", ooni_run_link_id=diccionarioPaises_ooni_actualizada[pais])