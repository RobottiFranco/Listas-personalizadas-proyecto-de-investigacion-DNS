import csv

from Clases.Consulta import Consulta
from Clases.helper.obtenerGrafico import obtener_grafico, obtener_grafico_mejorado
from Clases.helper.globalVariables import consulta_grafica as base_url

def comparacion(archivo1, archivo2):
    listaASN7303 = []
    listaASN16814 = []

    with open(archivo1, mode='r') as file1, open(archivo2, mode='r') as file2:
        reader1 = list(csv.DictReader(file1))  # Convertir a lista
        reader2 = list(csv.DictReader(file2))  # Convertir a lista
        
        for row1 in reader1:
            if row1 not in reader2:  # Compara filas como diccionarios
                listaASN7303.append(row1)
        for row2 in reader2:
            if (row2 not in reader1):
                listaASN16814.append(row2)
    print(f"conjunto1: {listaASN16814}")
    print("")
    print(f"conjunto2: {listaASN7303}")

com = comparacion("Listas_OONI/actualizada/AR_ACTUALIZADO_as7303.csv", "Listas_OONI/actualizada/AR_ACTUALIZADO_as16814.csv")

def graficar_lista_historica(mejorada: bool = False, asn: str = 0):
    consulta = Consulta(base_url, "web_connectivity", "AR", "2024-01-01", "2025-12-31", 10094, asn, None, None, None)
    if mejorada:
        obtener_grafico_mejorado(consulta, "month", "category_code", None, "ArgentinaPrueba", f"{asn}{mejorada}")
    else:
        obtener_grafico(consulta, "month", "category_code", None,"ArgentinaPrueba", f"{asn}{mejorada}")

graficar_lista_historica(True, "AS7303")
graficar_lista_historica(False, "AS7303")


graficar_lista_historica(True, "AS16814")
graficar_lista_historica(False, "AS16814")