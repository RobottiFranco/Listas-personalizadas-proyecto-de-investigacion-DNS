import time
import requests

class ClienteAPI:
    def __init__(self, url, retries):
        self.url = url
        self.retries = retries
        
    def _backoff(self, retry: int) -> int:
        return 2 ** retry

    def realizar_solicitud_obtencion(self):
        response = None
        for retry in range(self.retries):
            try:
                response = requests.get(self.url)
                response.raise_for_status()
                response = response.json()
            except requests.RequestException as e:
                wait_time = self._backoff(retry)
                print(f"Error al consultar {self.url}: {e}. Reintentando en {wait_time} segundos... (Intento {retry + 1}/{self.retries})")
                time.sleep(wait_time)
            except Exception as e:
                print(f"Error inesperado: {e}. Deteniendo los intentos.")
                response = None
        return response