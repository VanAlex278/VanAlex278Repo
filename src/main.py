from src.masks import process_bank_search, process_bank_operations
from src.processing import filter_by_state, sort_by_date
from src.reader import csv_file_reader, excel_file_reader
from src.utils import list_transaction_returned
from src.widget import get_date, mask_account_card


def main() -> None:
    list_transactions = selection_file()
    list_answers = selection_operations()
    modified_list = filter_by_state(list_transactions, list_answers[0])
    if list_answers[1] == "ПО ВОЗРАСТАНИЮ":
        modified_list = sort_by_date(modified_list, True)
    elif list_answers[1] == "ПО УБЫВАНИЮ":
        modified_list = sort_by_date(modified_list, False)
    if list_answers[2] == "ДА":
        modified_list2 = []
        for transaction in modified_list:
            if transaction["currency_code"] == "RUB":
                modified_list2.append(transaction)
        modified_list = modified_list2
    if list_answers[3] != "НЕТ":
        modified_list2 = process_bank_search(modified_list, list_answers[3])
        if modified_list2 == []:
            print("Транзакции с такими словами не найдены")
        else:
            modified_list = modified_list2
    if len(modified_list) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {process_bank_operations(modified_list)}")
        for transaction in modified_list:
            print(get_date(transaction["date"]), end=" ")
            print(transaction["description"])
            print(f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}")
            print(f"Сумма: {transaction["amount"]} {transaction["currency_code"]}")


def selection_file() -> list[dict]:
    """Функция выбора файла с транзакциями, возвращает список транзакций"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    while True:
        file_selection = input()
        if file_selection == "1":
            list_transactions = list_transaction_returned()
            print("Для обработки выбран JSON-файл.")
            break
        elif file_selection == "2":
            list_transactions = csv_file_reader()
            print("Для обработки выбран CSV-файл.")
            break
        elif file_selection == "3":
            list_transactions = excel_file_reader()
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Неверный ввод")
    return list_transactions


def selection_operations() -> list:
    """Функция для выбора пользовательских настроек сортировки транзакций"""
    print(
        "Программа: Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:"
        " EXECUTED, CANCELED, PENDING"
    )
    list_operation = ["EXECUTED", "CANCELED", "PENDING"]
    list_answers = []
    while True:
        selection_operation = input().upper()
        if selection_operation in list_operation:
            list_answers.append(selection_operation)
            break
        print("Неверный ввод")
    print(f"Операции отфильтрованы по статусу {selection_operation}")
    print("Отсортировать операции по дате? Да/Нет")
    while True:
        entering_answers = input().upper()
        if entering_answers == "ДА":
            print("Отсортировать по возрастанию или по убыванию?")
            while True:
                entering_answers2 = input().upper()
                if entering_answers2 == "ПО ВОЗРАСТАНИЮ":
                    list_answers.append("ПО ВОЗРОСТАНИЮ")
                    break
                elif entering_answers2 == "ПО УБЫВАНИЮ":
                    list_answers.append("ПО УБЫВАНИЮ")
                    break
                else:
                    print("Неверный ввод")
            break
        elif entering_answers == "НЕТ":
            list_answers.append("НЕТ")
            break
        else:
            print("Неверный ввод")
    print("Выводить только рублевые транзакции? Да/Нет")
    while True:
        entering_answers3 = input().upper()
        if entering_answers3 == "ДА":
            list_answers.append("ДА")
            break
        elif entering_answers3 == "НЕТ":
            list_answers.append("НЕТ")
            break
        else:
            print("Неверный ввод")
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    while True:
        entering_answers4 = input().upper()
        if entering_answers4 == "ДА":
            print("Введите слово для поиска")
            list_answers.append(input())
            break
        elif entering_answers4 == "НЕТ":
            list_answers.append("НЕТ")
            break
        else:
            print("Неверный ввод")
    print("Распечатываю итоговый список транзакций...")
    return list_answers


print(main())
