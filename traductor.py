import csv

""" funcion que toma un archivo .csv de OONI y lo transforma para su utilziacion de OONI run link"""
def traductorOONI(archivo, outName):
    with open(archivo, "r", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        with open(outName, "w", newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            for row in reader:
                    writer.writerow([row[0].strip()])
                    print(row[0].strip())

traductorOONI("ooniList\\ve.csv", "ooniList\\ve_run_link.csv")
traductorOONI("ooniList\\uy.csv", "ooniList\\uy_run_link.csv")

""" funcion que toma un archivo .csv de ipsvenezuela y lo transforma para su utilziacion de OONI run link"""
def traductorIpysvenezuela(archivo, outName):
    with open(archivo, "r", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        with open(outName, "w", newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            for row in reader:
                    writer.writerow([row[0].strip()])
                    print(row[0].strip())

traductorIpysvenezuela("ipysvenezuela.org\\ve.csv", "ipysvenezuela.org\\ve_run_link.csv")

