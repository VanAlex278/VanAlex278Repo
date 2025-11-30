import logging
from collections import Counter


logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | str) -> str:
    """Функцию маскировки номера банковской карты"""
    card_number1 = str(card_number)
    if len(card_number1) != 16 or not card_number1.isdigit():
        logger.warning(f'{card_number} wrong')
        return "Некорректный номер карты"
    card_mask = card_number1[:4] + " " + card_number1[4:6] + "** **** " + card_number1[-4:]
    logger.info(f'mask_card: {card_mask}')
    return card_mask


def get_mask_account(account_number: int | str) -> str:
    """Функцию маскировки номера банковского счета"""
    account_number1 = str(account_number)
    if len(account_number1) != 20 or not account_number1.isdigit():
        logger.warning(f'{account_number} wrong')
        return "Некорректный номер счета"
    account_mask = "**" + account_number1[-4:]
    logger.info(f'mask_account: {account_mask}')
    return account_mask


def process_bank_search(list_transactions:list[dict], search:str)->list[dict]:
    """Функция поиска строки в описании."""
    search_list = []
    for transac in list_transactions:
        if  search in transac["description"]:
            search_list.append(transac)
    return search_list


def process_bank_operations(list_transactions:list[dict], categories: str = "description") -> dict:
    """Функция статистики транзакций по категориям"""
    list_categories = []
    for i in list_transactions:
        list_categories.append(i[categories])
    counted = Counter(list_categories)
    return counted

if __name__ == "__main__":
    list_of_transactions = [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
        ]
    fff = process_bank_operations(list_of_transactions)
    print(fff)

