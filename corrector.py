import csv
import re

def corregir_csv(archivo_entrada, archivo_salida):
    """Corrige el formato de un archivo CSV con IDs, URLs y resoluciones."""
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
