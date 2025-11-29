import pandas as pd


def csv_file_reader(path_to_file: str = "../data/transactions.csv") -> list[dict] | list:
    """Функция чтения CSV-файла возвращает список словарей с данными о финансовых транзакциях"""
    list_csv_transactions = []
    try:
        csv_data = pd.read_csv(path_to_file, delimiter=";")
        return csv_data.to_dict(orient="records")
    except FileNotFoundError:
        return []


def excel_file_reader(path_to_excel_file: str = "../data/transactions_excel.xlsx") -> list[dict]:
    """Функция чтения Excel-файла возвращает список словарей с данными о финансовых транзакциях"""
    try:
        excel_data = pd.read_excel(path_to_excel_file)
        return excel_data.to_dict(orient="records")
    except FileNotFoundError:
        return []
