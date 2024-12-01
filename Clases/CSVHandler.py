import csv
import pandas as pd

class CSVHandler:
    def __init__(self):
        pass


    def filtrar_dns(self, datos):
        """ 
        Filtra los datos obtenidos de la API de OONI para obtener solo los resultados de bloqueo por DNS
        datos: datos en formato JSON obtenidos de la API de OONI por el metodo obtener_datos
        """
        result = []
        if "results" in datos:
            for item in datos["results"]:
                if item.get("scores", {}).get("analysis", {}).get("blocking_type") == "dns":
                    result.append(item)
        return result


    def eliminar_duplicados(self, datos):
        """ 
        Elimina los datos duplicados de la lista de datos
        datos: lista de datos en formato JSON obtenidos de la API de OONI por el metodo filtrar_dns
        """
        seen_inputs = set()
        result = []

        for item in datos:
            input_value = item.get("input")
            if input_value not in seen_inputs:
                result.append(item)
                seen_inputs.add(input_value)

        return result


    def guardar_en_csv(self, archivo_salida, datos, modo):
        """ 
        Guarda los datos en un archivo CSV
        datos: lista de datos que se guardarán en el archivo
        archivo_salida: ruta del archivo CSV donde se guardarán los datos
        modo: modo de apertura del archivo (por ejemplo, 'w' para escribir)
        """
        if datos:
            with open(archivo_salida, mode=modo, newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=datos[0].keys())
                writer.writeheader()
                writer.writerows(datos)
            print(f"Datos guardados en {archivo_salida}")
        else:
            print("No hay datos para guardar.")
            

    def compenetrar_csv(self, csv_file, archivo_salida):
        """ 
        Crea un archivo CSV con los links de OONI Run
        csv_file: archivo CSV con los datos de OONI Run
        archivo_salida: nombre del archivo CSV donde se guardarán los links
        """
        try:
            # Leer el archivo CSV
            df = pd.read_csv(csv_file)
            
            # Filtrar filas donde 'input' no es igual a 'input'
            df = df[df['input'].str.lower() != 'input']
            
            # Eliminar duplicados basados en la columna 'input'
            df_sin_repetidos = df.drop_duplicates(subset='input', keep='first')
            
            # Guardar solo la columna 'input' en el archivo de salida
            df_sin_repetidos[['input']].to_csv(archivo_salida, index=False)
            
            print(f"Archivo {csv_file} procesado y guardado como {archivo_salida}")
        
        except Exception as e:
            print(f"Error al procesar el archivo {csv_file}: {e}")