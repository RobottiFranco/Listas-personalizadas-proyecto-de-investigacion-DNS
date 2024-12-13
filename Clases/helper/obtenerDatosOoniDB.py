from Clases.Consulta import Consulta
from Clases.ClienteAPI import ClienteAPI
from Clases.CSVHandler import CSVHandler


def obtener_datos_ooni_db(consulta: Consulta , limit: int, anomaly: bool, directorio_salida: str, nombre_archivo: str, modo: str) -> None:
    print(f"Iniciando el proceso datos de {consulta.probe_cc}...")

    url = consulta
    url = url.armar_consulta_db(limit, anomaly)
    
    datos = ClienteAPI(url, 3)
    datos = datos.realizar_solicitud_obtencion()
    if datos is None:
        print(f"No se pudieron obtener datos de {consulta.probe_cc} desde {consulta.since} hasta {consulta.until}")
        return
    
    datos_filtrados = CSVHandler().filtrar_y_eliminar_duplicados(datos)
    
    ruta = CSVHandler().crear_archivo_y_ruta(directorio_salida, f"{nombre_archivo}.csv")
    CSVHandler().guardar_en_csv(ruta, datos_filtrados, modo)

def obtener_datos_ooni_db_actualizados(consulta: Consulta , limit: int, anomaly: bool, directorio_salida: str, nombre_archivo: str, modo: str) -> None:
    print(f"Iniciando el proceso datos de {consulta.probe_cc} {consulta.category_code}...")

    url = consulta
    url = url.armar_consulta_db(limit, anomaly)
    
    datos = ClienteAPI(url, 3)
    datos = datos.realizar_solicitud_obtencion()
    if datos is None:
        print(f"No se pudieron obtener datos de {consulta.probe_cc} desde {consulta.since} hasta {consulta.until}")
        return
    
    datos_filtrados = CSVHandler().filtrar_y_eliminar_duplicados(datos)
    
    ruta = CSVHandler().crear_archivo_y_ruta(directorio_salida, f"{nombre_archivo}.csv")
    CSVHandler().guardar_en_csv(ruta, datos_filtrados, modo, consulta.category_code)
