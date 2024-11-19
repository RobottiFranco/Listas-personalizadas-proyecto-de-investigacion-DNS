import os
from traductor import *

# argentina citizenlab
traductor("argentina\\ar-citizenlab.csv", "argentina\\ar-citizenlab-clear-temp.csv", 0, delimitador=',')
procesar_urls_y_agregar("argentina\\ar-citizenlab-clear-temp.csv", "argentina\\ar-citizenlab-clear.csv")
os.remove("argentina\\ar-citizenlab-clear-temp.csv")

# argentina telerium
traductor("argentina\\ar-telerium.csv", "argentina\\ar-telerium-clear-temp.csv", 0, delimitador=',')
procesar_urls_y_agregar("argentina\\ar-telerium-clear-temp.csv", "argentina\\ar-telerium-clear.csv")
os.remove("argentina\\ar-telerium-clear-temp.csv")

# argentina tribuna
traductor("argentina\\ar-tribuna.csv", "argentina\\ar-tribuna-clear-temp.csv", 0, delimitador=',')
procesar_urls_y_agregar("argentina\\ar-tribuna-clear-temp.csv", "argentina\\ar-tribuna-clear.csv")
os.remove("argentina\\ar-tribuna-clear-temp.csv")

# lista final argentina

agregar_csv_a_salida("argentina\\ar-citizenlab-clear.csv", "argentina\\ar-final-temp.csv")
agregar_csv_a_salida("argentina\\ar-telerium-clear.csv", "argentina\\ar-final-temp.csv")
agregar_csv_a_salida("argentina\\ar-tribuna-clear.csv", "argentina\\ar-final-temp.csv")

eliminar_duplicados("argentina\\ar-final-temp.csv", "ar-final.csv")
os.remove("argentina\\ar-final-temp.csv")