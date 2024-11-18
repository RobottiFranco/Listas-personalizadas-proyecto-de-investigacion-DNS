import csv

def eliminar_duplicados(archivo_entrada, archivo_salida):
    """
    Elimina duplicados de un archivo CSV de URLs y genera un nuevo archivo sin duplicados.

    Args:
        archivo_entrada (str): Ruta al archivo CSV de entrada con las URLs.
        archivo_salida (str): Ruta al archivo CSV donde se guardarán las URLs únicas.
    """
    urls_unicas = set()  # Usamos un set para almacenar URLs únicas

    # Leer el archivo de entrada y filtrar duplicados
    with open(archivo_entrada, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        for row in reader:
            if row:  # Evitar filas vacías
                url = row[0].strip()
                urls_unicas.add(url)  # Agregar solo URLs únicas

    # Escribir las URLs únicas al archivo de salida
    with open(archivo_salida, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        for url in sorted(urls_unicas):  # Ordenar las URLs opcionalmente
            writer.writerow([url])

    print(f"Se eliminaron duplicados y se guardaron {len(urls_unicas)} URLs únicas en '{archivo_salida}'.")
