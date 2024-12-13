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
    dns_consistency = test_keys.get("dns_consistency", "No disponible")
    dns_experiment_failure = test_keys.get("dns_experiment_failure", "No disponible")
    dns_addresses = ", ".join(test_keys.get("dns", {}).get("addrs", []))  # Convertir lista a string
    
    dns_requests = []
    if test_keys.get("requests") is not None:
        dns_requests = [req.get("failure", "No failure") for req in test_keys["requests"]]
    dns_requests_failures = "; ".join(dns_requests)

    row = {
        "measurement_uid": mesaurment_uid,
        "dns_consistency": dns_consistency,
        "dns_experiment_failure": dns_experiment_failure,
        "dns_addresses": dns_addresses,
        "dns_requests_failures": dns_requests_failures
    }
    
    ruta = CSVHandler().crear_archivo_y_ruta(nombre_salida, f"{archivo_salida}.csv")
    CSVHandler().guardar_en_csv_mod(ruta, row, "w")
