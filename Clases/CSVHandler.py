import csv
import os
import pandas as pd

from Clases.helper.globalVariables import diccionario_Paise_lista_ooni_historica

class CSVHandler:
    def __init__(self):
        pass


    def _filtrar_dns(self, datos: dict) -> list:
        result = []
        if "results" in datos:
            for item in datos["results"]:
                if item.get("scores", {}).get("analysis", {}).get("blocking_type") == "dns":
                    result.append(item)
        return result


    def _eliminar_duplicados(self, datos: list) -> list:
        seen_inputs = set()
        result = []

        for item in datos:
            input_value = item.get("input")
            if input_value not in seen_inputs:
                result.append(item)
                seen_inputs.add(input_value)

        return result
    
    
    def filtrar_y_eliminar_duplicados(self, datos: dict) -> list:
        return self._eliminar_duplicados(self._filtrar_dns(datos))


    def guardar_en_csv(self, archivo_salida: str, datos, modo: str):
        if datos:
            with open(archivo_salida, mode=modo, newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=datos[0].keys())
                writer.writeheader()
                writer.writerows(datos)
            print(f"Datos guardados en {archivo_salida}")
        else:
            print("No hay datos para guardar.")
            

    def _compenetrar_csv(self, archivo_entrada: str, archivo_salida: str) -> None:
        try:
            df = pd.read_csv(archivo_entrada)
            df = df[df['input'].str.lower() != 'input']
            df_sin_repetidos = df.drop_duplicates(subset='input', keep='first')
            df_sin_repetidos[['input']].to_csv(archivo_salida, index=False)
            
            print(f"Archivo {archivo_entrada} procesado y guardado como {archivo_salida}")
        
        except Exception as e:
            print(f"Error al procesar el archivo {archivo_entrada}: {e}")
            
            
    def _crear_archivo_y_ruta(self, base_dir: str, nombre_archivo: str) -> str:
        os.makedirs(base_dir, exist_ok=True)
        ruta_completa = os.path.join(base_dir, nombre_archivo)
        print(f"Ruta creada o verificada: {ruta_completa}")
        return ruta_completa
    
    def crear_ooni_run_link(self, archivo_entrada: str, nombre_archivo: str, directorio_salida: str) -> None:
        for pais in diccionario_Paise_lista_ooni_historica:
            archivo_salida = self._crear_archivo_y_ruta(directorio_salida, f"{pais}_{nombre_archivo}.csv")
            CSVHandler()._compenetrar_csv(archivo_entrada, archivo_salida)