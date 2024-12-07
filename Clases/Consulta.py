import urllib.parse

class Consulta:
    def __init__(self, base_url, test_name, probe_cc, since, until, ooni_run_link_id, probe_asn, domain, input, category_code):
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

    def _eliminar_parametros_nulos(self, parametros):
        return {k: v for k, v in parametros.items() if v is not None}

    def _armar_url(self, parametros):
        parametros = self._eliminar_parametros_nulos(parametros)
        return self.base_url + "?" + urllib.parse.urlencode(parametros, doseq=True)

    def armar_consulta_grafica(self, time_grain, axis_x, axis_y):
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

    def armar_consulta_db(self, limit, anomaly):
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
