
from traductor import traductor
from corrector import corregir_csv

#traductor
traductor("uruguay\\uy-citizenlab.csv", "uruguay\\uy-citizenlab-clear.csv", 0, delimitador=',')
traductor("uruguay\\uy-2023-2024.csv", "uruguay\\uy-2023-2024-clear.csv", 1, delimitador=';')

#corregir_csv
