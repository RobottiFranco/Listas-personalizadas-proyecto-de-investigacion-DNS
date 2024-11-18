import csv

""" funcion que toma un archivo .csv y lo transforma para su utilizacion de OONI run link"""
""" toma el archivo original y el nombre del archivo de salida, la columna que se desea traducir y el tipo de delimitador"""
def traductor(archivo=str, outName=str, columna=0, delimitador=','):
    with open(archivo, "r", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimitador)
        with open(outName, "w", newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            for row in reader:
                try:
                    if row[columna].strip() != "":
                        writer.writerow([row[columna].strip()])
                except IndexError:
                    print(f"Elemento saltado: {row}")