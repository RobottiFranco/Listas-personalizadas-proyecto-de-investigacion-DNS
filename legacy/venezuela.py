
import os
from traductor import *

# venezuela citizenlab
traductor("venezuela\\ve-citizenlab.csv", "venezuela\\ve-citizenlab-clear-temp.csv", 0, delimitador=',')
procesar_urls_y_agregar("venezuela\\ve-citizenlab-clear-temp.csv", "venezuela\\ve-citizenlab-clear.csv")
os.remove("venezuela\\ve-citizenlab-clear-temp.csv")

# venezuela ipysvenezuela
traductor("venezuela\\ve-ipysvenezuela.csv", "venezuela\\ve-ipysvenezuela-clear-temp.csv", 1, delimitador=',')
procesar_urls_y_agregar("venezuela\\ve-ipysvenezuela-clear-temp.csv", "venezuela\\ve-ipysvenezuela-clear.csv")
os.remove("venezuela\\ve-ipysvenezuela-clear-temp.csv")

# lista final venezuela

agregar_csv_a_salida("venezuela\\ve-citizenlab-clear.csv", "venezuela\\ve-final-temp.csv")
agregar_csv_a_salida("venezuela\\ve-ipysvenezuela-clear.csv", "venezuela\\ve-final-temp.csv")

eliminar_duplicados("venezuela\\ve-final-temp.csv", "ve-final.csv")

os.remove("venezuela\\ve-final-temp.csv")