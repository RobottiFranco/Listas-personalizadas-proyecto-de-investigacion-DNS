
from eliminarDuplicados import eliminar_duplicados
from formateo import procesar_urls_y_agregar
from traductor import traductor
from corrector import corregir_csv

#traductor
traductor("uruguay\\uy-citizenlab.csv", "uruguay\\uy-citizenlab-clear.csv", 0, delimitador=',')
traductor("uruguay\\uy-2023-2024.csv", "uruguay\\uy-2023-2024-clear.csv", 1, delimitador=';')

#corregir_csv

corregir_csv("uruguay\\uy-2018enAdelante.csv", "uruguay\\uy-2018enAdelante-arreglado.csv")

#traductor
traductor("uruguay\\uy-2018enAdelante-arreglado.csv", "uruguay\\uy-2018enAdelante-arreglado-clear.csv", 1, delimitador=',')

#formateo final
procesar_urls_y_agregar("uruguay\\uy-2023-2024-clear.csv", "final Uruguay.csv")
procesar_urls_y_agregar("uruguay\\uy-2018enAdelante-arreglado-clear.csv", "final Uruguay.csv")
procesar_urls_y_agregar("uruguay\\uy-citizenlab.csv", "final Uruguay.csv")

eliminar_duplicados("final Uruguay.csv", "final_Uruguay_2.csv")
