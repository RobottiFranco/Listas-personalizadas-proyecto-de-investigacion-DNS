import csv

def procesar_urls_y_agregar(archivo_entrada, archivo_salida):
    """
    Procesa un archivo de URLs, agrega variantes con 'http://www.' y 'https://www.' para las URLs
    que no las tienen, y las escribe en un archivo de salida.

    Args:
        archivo_entrada (str): Ruta al archivo CSV de entrada con las URLs.
        archivo_salida (str): Ruta al archivo CSV donde se agregarán las URLs procesadas.
    """
    urls_procesadas = []

    # Leer las URLs desde el archivo de entrada
    with open(archivo_entrada, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        for row in reader:
            if row:  # Evitar filas vacías
                url = row[0].strip()  # Tomar la URL de la primera columna
                if url.startswith("http://www.") or url.startswith("https://www."):
                    urls_procesadas.append([url])  # Si ya tiene el formato correcto
                else:
                    # Agregar las dos variantes si no tiene el prefijo correcto
                    urls_procesadas.append([f"http://www.{url.lstrip('www.')}"])
                    urls_procesadas.append([f"https://www.{url.lstrip('www.')}"])

    # Escribir las URLs procesadas al archivo de salida
    with open(archivo_salida, "a", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerows(urls_procesadas)

    print(f"Se procesaron {len(urls_procesadas)} URLs y se agregaron al archivo '{archivo_salida}'.")