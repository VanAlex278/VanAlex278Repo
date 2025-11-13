import json
from idlelib.iomenu import encoding


def list_transaction_returned(path_to_json_file='../data/operations.json') -> list:
    """Функция чтения JSON-файла возвращает список словарей с данными о финансовых транзакциях"""
    if path_to_json_file == None:
        return []
    else:
        with open(path_to_json_file, encoding="utf-8") as f:
            list_transaction = json.load(f)
        return list_transaction

data = list_transaction_returned()
print(data)
