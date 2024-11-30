from Clases.Consulta import *

def test_consulta_grafica_completa():
    expected = (
        "https://explorer.ooni.org/api/aggregation?"
        "probe_cc=UY&since=2024-01-01&until=2024-12-31&"
        "time_grain=day&axis_x=time&test_name=web_connectivity&"
        "ooni_run_link_id=1234"
    )
        
    url = Consulta(
        probe_cc="UY",
        since="2024-01-01",
        until="2024-12-31",
        ooni_run_link_id="1234"
    ).armar_consulta_grafica(
        time_grain="day",
        axis_x="time",
        test_name="web_connectivity"
    )
    assert url == expected
    
def test_consulta_grafica_completa_sin_ooni_run_link_id():
    expected = (
        "https://explorer.ooni.org/api/aggregation?"
        "probe_cc=UY&since=2024-01-01&until=2024-12-31&"
        "time_grain=day&axis_x=time&test_name=web_connectivity"
    )
        
    url = Consulta(
        probe_cc="UY",
        since="2024-01-01",
        until="2024-12-31",
    ).armar_consulta_grafica(
        time_grain="day",
        axis_x="time",
        test_name="web_connectivity"
    )
    assert url == expected
    
    
def test_consulta_db_OONI_completa():
    expected = (
        "https://api.ooni.io/api/v1/measurements?"
        "limit=10&probe_cc=UY&test_name=web_connectivity&"
        "since=2024-01-01&until=2024-12-31&anomaly=True&ooni_run_link_id=1234"
    )
        
    url = Consulta(
        probe_cc="UY",
        since="2024-01-01",
        until="2024-12-31",
        ooni_run_link_id="1234"
    ).armar_consulta_db_OONI(
        limit=10,
        anomaly=True,
        test_name="web_connectivity"
    )
    assert url == expected
    
def test_consulta_db_OONI_sin_ooni_run_link_id():
    expected = (
        "https://api.ooni.io/api/v1/measurements?"
        "limit=10&probe_cc=UY&test_name=web_connectivity&"
        "since=2024-01-01&until=2024-12-31&anomaly=True"
    )
        
    url = Consulta(
        probe_cc="UY",
        since="2024-01-01",
        until="2024-12-31"
    ).armar_consulta_db_OONI(
        limit=10,
        anomaly=True,
        test_name="web_connectivity"
    )
    assert url == expected