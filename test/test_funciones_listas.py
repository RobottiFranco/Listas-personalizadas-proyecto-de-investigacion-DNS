from Funciones.FuncionesListas import *
from unittest.mock import patch

def test_consulta_con_parametros_completos():
    url = consulta(
        limit=10,
        probe_cc="UY",
        since="2024-01-01",
        until="2024-12-31",
        anomaly=True,
        ooni_run_link_id="1234"
    )
    expected = (
        "https://api.ooni.org/api/v1/measurements?"
        "limit=10&probe_cc=UY&test_name=web_connectivity&"
        "since=2024-01-01&until=2024-12-31&anomaly=True&ooni_run_link_id=1234"
    )
    assert url == expected

def test_consulta_sin_ooni_run_link_id():
    url = consulta(
        limit=5,
        probe_cc="BR",
        since="2023-01-01",
        until="2023-12-31",
        anomaly=False
    )
    expected = (
        "https://api.ooni.org/api/v1/measurements?"
        "limit=5&probe_cc=BR&test_name=web_connectivity&"
        "since=2023-01-01&until=2023-12-31&anomaly=False"
    )
    assert url == expected
    

@patch("requests.get")
def test_obtener_datos_exito(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"results": []}
    
    url = "https://api.ooni.org/api/v1/measurements?test=ok"
    response = obtener_datos(url)
    
    assert response == {"results": []}
    mock_get.assert_called_once_with(url)

@patch("requests.get")
def test_obtener_datos_error(mock_get):
    mock_get.side_effect = requests.RequestException("Error de red")
    
    url = "https://api.ooni.org/api/v1/measurements?test=error"
    response = obtener_datos(url, retries=2)
    
    assert response is None
    assert mock_get.call_count == 2
    

def test_filtrar_dns():
    datos = {
        "results": [
            {"scores": {"analysis": {"blocking_type": "dns"}}, "input": "example.com"},
            {"scores": {"analysis": {"blocking_type": "http"}}, "input": "other.com"},
        ]
    }
    filtrados = filtrar_dns(datos)
    assert len(filtrados) == 1
    assert filtrados[0]["input"] == "example.com"
    

def test_eliminar_duplicados():
    datos = [
        {"input": "example.com", "data": "data1"},
        {"input": "example.com", "data": "data1"},
        {"input": "other.com", "data": "data2"},
    ]
    sin_duplicados = eliminar_duplicados(datos)
    assert len(sin_duplicados) == 2
    assert sin_duplicados[0]["input"] == "example.com"
    assert sin_duplicados[1]["input"] == "other.com"    
    
    
from unittest.mock import mock_open, patch
from Funciones.FuncionesListas import guardar_en_csv

@patch("builtins.open", new_callable=mock_open)
def test_guardar_en_csv(mock_file):
    datos = [{"input": "example.com", "data": "data1"}]
    guardar_en_csv(datos, "output.csv", "w")
    
    mock_file.assert_called_once_with("output.csv", mode="w", newline="", encoding="utf-8")
    handle = mock_file()
    handle.write.assert_called()  # Verifica que se escribió algo en el archivo


