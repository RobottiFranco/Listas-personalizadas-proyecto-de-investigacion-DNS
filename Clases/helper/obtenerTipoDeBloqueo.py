from Clases.CSVHandler import CSVHandler
from Clases.ClienteAPI import ClienteAPI
from Clases.Consulta import Consulta
from Clases.helper.globalVariables import consulta_obtener_datos_bloqueo


def obtener_tipo_de_bloqueo(mesaurment_uid: str, nombre_salida: str, archivo_salida: str):
    url  = Consulta(consulta_obtener_datos_bloqueo)
    url = url.armar_consulta_datos_bloqueo(mesaurment_uid)
    print(url)
    datos = ClienteAPI(url, 3)
    datos = datos.realizar_solicitud_obtencion()

    test_keys = datos.get("test_keys", {})
    http_request = test_keys.get("control", {}).get("http_request", {})


    row = {
        "measurement_uid": mesaurment_uid or "None",
        "dns_experiment_failure": test_keys.get("dns_experiment_failure", "None") or "None",
        "http_experiment_failure": test_keys.get("http_experiment_failure", "None") or "None",
        "accessible": test_keys.get("accessible") if "accessible" in test_keys else "None",
        "blocking": test_keys.get("blocking", "None") or "None",
        "resolver_asn": datos.get("resolver_asn", "None") or "None",
        "status_code": http_request.get("status_code", "None") or "None",
    }
    
    ruta = CSVHandler().crear_archivo_y_ruta(nombre_salida, f"{archivo_salida}.csv")
    CSVHandler().escribir_tipo_de_bloqueo_csv(ruta, [row], "a")
