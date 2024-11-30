import time
import requests
from unittest.mock import patch, Mock
from Clases.ClienteAPI import *

# Test de éxito: la solicitud HTTP devuelve una respuesta exitosa
@patch('requests.get')
def test_realizar_solicitud_obtencion_success(mock_get):
    # Preparar la respuesta mockeada
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None  # Simula un estado exitoso
    mock_response.json.return_value = {"data": "test"}  # Datos que devuelve la API
    mock_get.return_value = mock_response
    
    # Crear una instancia de ClienteAPI
    cliente = ClienteAPI("http://api.test.com", retries=3)
    
    # Ejecutar el método que queremos testear
    resultado = cliente.realizar_solicitud_obtencion()
    
    # Verificar que la respuesta es la esperada
    assert resultado == {"data": "test"}
    mock_get.assert_called_once_with("http://api.test.com")  # Verificar que se hizo la solicitud correcta


# Test de fallo: la solicitud HTTP falla y se deben intentar reintentos
@patch('requests.get')
def test_realizar_solicitud_obtencion_failure(mock_get):
    # Preparar la respuesta mockeada para que falle
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("Error en la solicitud")
    mock_get.return_value = mock_response
    
    # Crear una instancia de ClienteAPI
    cliente = ClienteAPI("http://api.test.com", retries=2)
    
    # Ejecutar el método que queremos testear
    resultado = cliente.realizar_solicitud_obtencion()
    
    # Verificar que se devuelve None en caso de error
    assert resultado is None
    mock_get.assert_called_with("http://api.test.com")  # Verificar que se hizo la solicitud correcta


# Test de backoff: verificar el comportamiento de la función _backoff
def test_backoff():
    cliente = ClienteAPI("http://api.test.com", retries=3)
    
    # Verificar que el backoff funcione correctamente
    assert cliente._backoff(0) == 1
    assert cliente._backoff(1) == 2
    assert cliente._backoff(2) == 4


# Test de múltiples reintentos: la solicitud falla en los primeros intentos y luego tiene éxito
@patch('requests.get')
def test_realizar_solicitud_obtencion_multiple_retries(mock_get):
    # Simulamos que la solicitud falla 2 veces y tiene éxito en el tercer intento
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"data": "test"}

    # Simulamos el fallo en los primeros dos intentos
    mock_get.side_effect = [
        requests.exceptions.RequestException("Error en la solicitud"),
        requests.exceptions.RequestException("Error en la solicitud"),
        mock_response
    ]
    
    cliente = ClienteAPI("http://api.test.com", retries=3)
    
    # Ejecutar el método que queremos testear
    resultado = cliente.realizar_solicitud_obtencion()
    
    # Verificar que la respuesta es la esperada
    assert resultado == {"data": "test"}
    assert mock_get.call_count == 3  # Verificar que se intentaron 3 veces
