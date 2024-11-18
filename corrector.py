import csv
import re

def corregir_csv(archivo_entrada, archivo_salida):
    """Corrige el formato de un archivo CSV con URLs y resoluciones."""
    with open(archivo_entrada, "r", encoding="utf-8") as infile:
        lines = infile.readlines()
    
    # Variables de procesamiento
    data = []
    current_resolution = None
    url_pattern = re.compile(r"^(?:\d+\s)?(https?://|www\.).+")  # Detecta URLs con o sin número

    # Procesar líneas
    for line in lines:
        line = line.strip()
        
        if line.startswith("Resolución Nº"):
            current_resolution = line  # Actualiza la resolución activa
        elif url_pattern.match(line):
            # Limpia el URL
            line = re.sub(r"\s+", "", line)  # Quita espacios
            line = re.sub(r"^ttps://", "https://", line)  # Corrige ttps
            url_parts = line.split(" ", 1)  # Divide en ID y URL (si aplica)
            
            if len(url_parts) == 2:
                id_, url = url_parts
            else:
                id_, url = "", url_parts[0]
            
            # Agrega a la lista de datos
            data.append([id_, url, current_resolution])

    # Escribir archivo corregido
    with open(archivo_salida, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["ID", "URL", "Resolución"])  # Encabezado
        writer.writerows(data)

""" # Usar la función
corregir_csv("archivo_original.csv", "archivo_corregido.csv")
 """