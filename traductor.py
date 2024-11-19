import csv
import re

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
                    
                    

def corregir_csv(archivo_entrada, archivo_salida):
    with open(archivo_entrada, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    data = []
    current_resolution = None
    url_pattern = re.compile(r"^\s*(\d+)\s*(https?://|www\.)")  # Detecta IDs y URLs válidos

    for line in lines:
        line = line.strip()
        
        if line.startswith("Resolución Nº"):
            current_resolution = line  # Actualiza la resolución activa
        elif url_pattern.match(line):
            match = url_pattern.match(line)
            id_ = match.group(1)  # Extrae el ID
            url = line[len(id_):].strip()  # Remueve el ID de la línea
            url = re.sub(r"\s+", "", url)  # Quita espacios dentro del URL
            url = re.sub(r"^ttps://", "https://", url)  # Corrige "ttps://"
            data.append([id_, url, current_resolution])  # Agrega a la lista de datos

    with open(archivo_salida, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["ID", "URL", "Resolución"])  # Encabezado
        writer.writerows(data)



def procesar_urls_y_agregar(archivo_entrada, archivo_salida):
    urls_procesadas = []

    # Leer las URLs desde el archivo de entrada
    with open(archivo_entrada, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        for row in reader:
            if row:  # Evitar filas vacías
                url = row[0].strip()  # Tomar la URL de la primera columna

                # Si no tiene prefijo, agregamos ambas variantes
                if not (url.startswith("http://") or url.startswith("https://")):
                    urls_procesadas.append(f"http://{url}")
                    urls_procesadas.append(f"https://{url}")
                
                # Si tiene 'http://', no agregamos la variante 'https://'
                elif url.startswith("http://") and not url.startswith("https://"):
                    urls_procesadas.append(url)
                
                # Si tiene 'https://', no agregamos la variante 'http://'
                elif url.startswith("https://") and not url.startswith("http://"):
                    urls_procesadas.append(url)

    # Escribir las URLs procesadas al archivo de salida
    with open(archivo_salida, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        for url in set(urls_procesadas):  # Eliminar duplicados y escribir URLs únicas
            writer.writerow([url])

    print(f"Se procesaron {len(urls_procesadas)} URLs y se agregaron al archivo '{archivo_salida}'.")


    # Escribir las URLs procesadas al archivo de salida
    with open(archivo_salida, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        for url in set(urls_procesadas):  # Eliminar duplicados y escribir URLs únicas
            writer.writerow([url])

    print(f"Se procesaron {len(urls_procesadas)} URLs y se agregaron al archivo '{archivo_salida}'.")



def eliminar_duplicados(archivo_entrada, archivo_salida):
    urls_unicas = set()  # Usamos un set para almacenar URLs únicas\
    
    # Definir los patrones no deseados
    patrones_no_deseados = [
        "o dominio denunciado",
        "http://www.url",
        "https://www.url"
    ]

    # Leer el archivo de entrada y filtrar duplicados y las URLs no deseadas
    with open(archivo_entrada, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        for row in reader:
            if row:  # Evitar filas vacías
                url = row[0].strip()

                # Filtrar URLs no deseadas
                if not any(patron in url for patron in patrones_no_deseados):
                    urls_unicas.add(url.lower())  # Agregar solo URLs únicas que no contengan patrones no deseados

    # Escribir las URLs únicas al archivo de salida
    with open(archivo_salida, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        for url in sorted(urls_unicas):  # Ordenar las URLs opcionalmente
            writer.writerow([url])

    print(f"Se eliminaron duplicados y URLs no deseadas, y se guardaron {len(urls_unicas)} URLs válidas en '{archivo_salida}'.")

def agregar_csv_a_salida(archivo_entrada, archivo_salida):
    try:
        # Abrir el archivo de salida en modo append
        with open(archivo_salida, mode='a', newline='', encoding='utf-8') as archivo_salida_csv:
            writer = csv.writer(archivo_salida_csv)

            # Abrir el archivo de entrada en modo lectura
            with open(archivo_entrada, mode='r', newline='', encoding='utf-8') as archivo_entrada_csv:
                reader = csv.reader(archivo_entrada_csv)
                
                # Escribir las filas del archivo de entrada al archivo de salida
                for fila in reader:
                    writer.writerow(fila)

        print(f"Contenido de {archivo_entrada} agregado al final de {archivo_salida}.")
    
    except Exception as e:
        print(f"Error al procesar los archivos: {e}")