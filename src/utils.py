import json
from json import JSONDecodeError


def list_transaction_returned(path_to_json_file='../data/operations.json') -> list:
    """Функция чтения JSON-файла возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path_to_json_file, encoding="utf-8") as f:
            list_transaction = json.load(f)
            if list_transaction is None:
                return []
            elif type(list_transaction) is list:
                return []
        return list_transaction
    except (FileNotFoundError, JSONDecodeError) as e:
        print(f"Файл отсутствует или повреждён! {e}")
        return []
