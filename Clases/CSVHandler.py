import csv

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