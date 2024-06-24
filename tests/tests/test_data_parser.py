import pytest
from blne.data_parser import DataParser

def test_parse_json_success():
    data = '{"key": "value"}'
    result = DataParser.parse_json(data)
    assert result == {"key": "value"}

def test_parse_json_failure():
    data = 'invalid json'
    result = DataParser.parse_json(data)
    assert result is None

def test_parse_iot_data_success():
    data = "temp:25.5;humidity:60"
    result = DataParser.parse_iot_data(data)
    assert result == {"temp": "25.5", "humidity": "60"}

def test_parse_iot_data_failure():
    data = "invalid:data:format"
    result = DataParser.parse_iot_data(data)
    assert result is None

def test_validate_data_success():
    data = {"name": "John", "age": 30}
    schema = {"name": str, "age": int}
    result = DataParser.validate_data(data, schema)
    assert result is True

def test_validate_data_failure():
    data = {"name": "John", "age": "30"}
    schema = {"name": str, "age": int}
    result = DataParser.validate_data(data, schema)
    assert result is False
