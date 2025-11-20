from unittest.mock import patch
import requests
from src.external_api import currency_conversion


@patch('requests.get')
def test_currency_conversion(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'result': '100'}
    assert currency_conversion({"operationAmount": {"amount": "1", "currency": {"code": "EUR"}}}) == 100.0
