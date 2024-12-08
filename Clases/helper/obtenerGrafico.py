from Clases.Consulta import Consulta
from Clases.ClienteAPI import ClienteAPI
from Clases.CSVHandler import CSVHandler
from Clases.Grafico import Grafico


def obtener_grafico(consulta: Consulta, time_grain: str, axis_x: str, axis_y: str, directorio_salida: str, nombre_archivo: str) -> None:
    print(f"Iniciando el proceso grafico de {consulta.probe_cc}...")
    
    url = consulta
    url = url.armar_consulta_grafica(time_grain, axis_x, axis_y)
    
    datos = ClienteAPI(url, 3)
    datos = datos.realizar_solicitud_obtencion()
    if datos is None:
        print(f"No se pudieron obtener datos de {consulta.probe_cc} desde {consulta.since} hasta {consulta.until}")
        return

    grafico = Grafico(datos, consulta.probe_cc, consulta.ooni_run_link_id)
    grafico.graficarBarrasAnomalias()
    
    ruta = CSVHandler().crear_archivo_y_ruta(directorio_salida, f"{nombre_archivo}.png")
    grafico.guardarGrafico(ruta)