import urllib.parse

class Consulta:
    def __init__(self, probe_cc, since, until, ooni_run_link_id=None):
        self.probe_cc = probe_cc
        self.since = since
        self.until = until
        self.ooni_run_link_id = ooni_run_link_id
    
    
    def _agregar_ooni_run_link_id(self, parametros):
        if self.ooni_run_link_id is not None:
            parametros["ooni_run_link_id"] = self.ooni_run_link_id
        return parametros
    
    
    def armar_url(self, parametros, base_url):
        return base_url + urllib.parse.urlencode(parametros, doseq=True)
    
    
    def armar_consulta_grafica(self, time_grain, axis_x, test_name):
        base_url = "https://api.ooni.org/api/v1/aggregation?"
        parametros = {
            "probe_cc": self.probe_cc,
            "since": self.since,
            "until": self.until,
            "time_grain": time_grain,
            "axis_x": axis_x,
            "test_name": test_name,
        }
        
        parametros = self._agregar_ooni_run_link_id(parametros)
        
        return self.armar_url(parametros, base_url)
    
        
    def armar_consulta_db_OONI(self, limit, anomaly, test_name):
        base_url = "https://api.ooni.org/api/v1/measurements?"
        parametros = {
            "limit": limit,
            "probe_cc": self.probe_cc,
            "test_name": test_name,
            "since": self.since,
            "until": self.until,
            "anomaly": anomaly
        }

        parametros = self._agregar_ooni_run_link_id(parametros)
        
        return self.armar_url(parametros, base_url)