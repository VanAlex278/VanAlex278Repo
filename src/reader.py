import csv

import pandas as pd


def csv_file_reader(path_to_file: str = "../data/transactions.csv") -> list[dict] | list:
    """Функция чтения CSV-файла возвращает список словарей с данными о финансовых транзакциях"""
    list_csv_transactions = []
    try:
        with open(path_to_file, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                list_csv_transactions.append(row)
            return list_csv_transactions
    except FileNotFoundError:
        return []


def reader_excel_file(path_to_excel_file: str = "../data/transactions_excel.xlsx") -> list[dict]:
    """Функция чтения Excel-файла возвращает список словарей с данными о финансовых транзакциях"""
    try:
        excel_data = pd.read_excel(path_to_excel_file)
        return excel_data.to_dict(orient="records")
    except FileNotFoundError:
        return []


# if __name__ == '__main__':
#     df = reader_excel_file()
#     print(df)
