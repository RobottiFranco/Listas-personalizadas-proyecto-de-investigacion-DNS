import os
from Clases.Facade import *

os.makedirs("Listas_de_OONI_actualizada", exist_ok=True)
""" 
for pais in diccionarioPaises_ooni_historica:
    crearOnniRunLink(f"Base_de_datos_actualizada\\{pais}-{diccionarioPaises_ooni_historica['UY']}.csv", f"Listas_de_OONI_actualizada\\{pais}_ACTUALIZADA.csv")
 """
#1 - Extraer datos de OONI y crear lista personalizada historica
#extraer_datos()
#crearOnniRunLink()

#2 - Extraer datos de personalizada historica y crear lista personalizada actualizada
#extraer_datos_listaHistorica()
#crearOnniRunLink_partiendo_de_historica()

#3 - Graficar
graficar()