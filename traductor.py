import csv

""" funcion que toma un archivo .csv y lo transforma para su utilizacion de OONI run link"""
""" toma el archivo original y el nombre del archivo de salida, y la columna que se desea traducir"""
def traductor(archivo, outName, columna):
    with open(archivo, "r", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        with open(outName, "w", newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            for row in reader:
                if row[columna].strip() != "":
                    writer.writerow([row[columna].strip()])
                    print(row[columna].strip())

traductor("ooniList\\ve.csv", "ooniList\\ve_run_link.csv", 0)
traductor("ooniList\\uy.csv", "ooniList\\uy_run_link.csv", 0)
traductor("ipysvenezuela.org\\ve.csv", "ipysvenezuela.org\\ve_run_link.csv", 1)