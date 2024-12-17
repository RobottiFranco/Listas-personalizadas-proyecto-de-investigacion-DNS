import urllib.parse

class Consulta:
    def __init__(self, base_url: str, test_name: str = None, probe_cc: str = None, since: str = None, until: str = None, ooni_run_link_id: int = None, probe_asn: int = None, domain: str = None, input: str = None, category_code: str = None):
        self.base_url = base_url
        self.test_name = test_name
        self.probe_cc = probe_cc
        self.since = since
        self.until = until
        self.ooni_run_link_id = ooni_run_link_id
        self.probe_asn = probe_asn
        self.domain = domain
        self.input = input
        self.category_code = category_code

    def _eliminar_parametros_nulos(self, parametros: dict) -> dict:
        return {k: v for k, v in parametros.items() if v is not None}

    def _armar_url(self, parametros: dict) -> str:
        parametros = self._eliminar_parametros_nulos(parametros)
        return self.base_url + "?" + urllib.parse.urlencode(parametros, doseq=True)

    def armar_consulta_grafica(self, time_grain: str, axis_x: str, axis_y: str) -> str:
        parametros = {
            "probe_cc": self.probe_cc,
            "probe_asn": self.probe_asn,
            "since": self.since,
            "until": self.until,
            "time_grain": time_grain,
            "axis_x": axis_x,
            "axis_y": axis_y,
            "test_name": self.test_name,
            "domain": self.domain,
            "input": self.input,
            "category_code": self.category_code,
            "ooni_run_link_id": self.ooni_run_link_id,
        }
        return self._armar_url(parametros)

    def armar_consulta_db(self, limit: int, anomaly: bool) -> str:
        parametros = {
            "probe_cc": self.probe_cc,
            "probe_asn": self.probe_asn,
            "since": self.since,
            "until": self.until,
            "limit": limit,
            "anomaly": anomaly,
            "test_name": self.test_name,
            "domain": self.domain,
            "input": self.input,
            "ooni_run_link_id": self.ooni_run_link_id,
            "category_code": self.category_code,
        }
        return self._armar_url(parametros)

    def armar_consulta_datos_bloqueo(self, measurement_uid: str) -> str:
        parametros = {
            "measurement_uid": measurement_uid,
        }
        return self._armar_url(parametros)