from unittest.mock import patch
from src.reader import csv_file_reader, excel_file_reader


@patch("pandas.read_csv")
def test_csv_file_reader(mock_csv):
    expected = [{"test_key": "test_value"}]
    mock_csv.return_value.to_dict.return_value = expected
    result = csv_file_reader("test_file")
    assert result == expected


@patch("pandas.read_excel")
def test_excel_file_reader(mock_excel):
    expected = [{"test_key": "test_value"}]
    mock_excel.return_value.to_dict.return_value = expected
    result = excel_file_reader("test_file")
    assert result == expected