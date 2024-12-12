

import csv
from Clases.CSVHandler import CSVHandler
from Clases.helper.obtenerTipoDeBloqueo import obtener_tipo_de_bloqueo


def tipo_de_bloqueo(archivo_entrada: str, nombre_salida: str, archivo_salida: str):
    measurement_uids = []
    with open(archivo_entrada, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            measurement_uids.append(row.get('measurement_uid', None))

    for measurement_uid in measurement_uids:
        obtener_tipo_de_bloqueo(measurement_uid, nombre_salida, archivo_salida)
    
    

# Main

tipo_de_bloqueo("Base_de_datos/actualizada/UY.csv", "tipo_de_bloqueo", "UY")