
import os
from traductor import *

# uruguay citizenlab
traductor("uruguay\\uy-citizenlab.csv", "uruguay\\uy-citizenlab-clear-temp.csv", 0, delimitador=',')
procesar_urls_y_agregar("uruguay\\uy-citizenlab-clear-temp.csv", "uruguay\\uy-citizenlab-clear.csv")
os.remove("uruguay\\uy-citizenlab-clear-temp.csv")

# uruguay 2018 en adelante
corregir_csv("uruguay\\uy-2018enAdelante.csv", "uruguay\\uy-2018enAdelante-clear.csv")
traductor("uruguay\\uy-2018enAdelante-clear.csv", "uruguay\\uy-2018enAdelante-clear-temp.csv", 1, delimitador=',')
procesar_urls_y_agregar("uruguay\\uy-2018enAdelante-clear-temp.csv", "uruguay\\uy-2018enAdelante-clear.csv")
os.remove("uruguay\\uy-2018enAdelante-clear-temp.csv")

# uruguay 2023 - 2024
traductor("uruguay\\uy-2023-2024.csv", "uruguay\\uy-2023-2024-clear-temp.csv", 1, delimitador=';')
procesar_urls_y_agregar("uruguay\\uy-2023-2024-clear-temp.csv", "uruguay\\uy-2023-2024-clear.csv")
os.remove("uruguay\\uy-2023-2024-clear-temp.csv")

# lista final uruguay

agregar_csv_a_salida("uruguay\\uy-citizenlab-clear.csv", "uruguay\\uy-final-temp.csv")
agregar_csv_a_salida("uruguay\\uy-2018enAdelante-clear.csv", "uruguay\\uy-final-temp.csv")
agregar_csv_a_salida("uruguay\\uy-2023-2024-clear.csv", "uruguay\\uy-final-temp.csv")

eliminar_duplicados("uruguay\\uy-final-temp.csv", "uy-final.csv")
os.remove("uruguay\\uy-final-temp.csv")