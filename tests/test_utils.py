from unittest.mock import patch, mock_open
from src.utils import list_transaction_returned


@patch("json.load")
def test_list_transaction_returned(mock_load):
    with patch("builtins.open", mock_open()) as mocked_open:
        mock_load.return_value = {'test_1': 'test_data'}
        result = list_transaction_returned("dummy data")
        expected = {'test_1': 'test_data'}
        assert result == expected
