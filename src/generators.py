from typing import Generator


def filter_by_currency(list_transactions: list[dict[str, int]], name_of_currency: str = "RUB") -> Generator:
    """Функция принимает на вход список словарей, представляющих транзакции и заданную валюту.
    Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной."""
    for transaction in list_transactions:
        if transaction["operationAmount"]["currency"]["code"] == name_of_currency:
            yield transaction


def transaction_descriptions(list_transactions: list[dict[str, int]]) -> str:
    """Функция принимает на вход список словарей, представляющих транзакции и
    возвращает описание каждой операции по очереди."""
    for transaction in list_transactions:
        yield str(transaction["description"])


def card_number_generator(start_number: int, stop_number: int) -> Generator:
    """Генератор номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number_card in range(start_number, stop_number + 1):
        number_card_str = str(number_card)
        list_number_card = (16 - len(number_card_str)) * "0" + number_card_str
        yield list_number_card[:4] + " " + list_number_card[4:8] + " " + list_number_card[
            8:12
        ] + " " + list_number_card[12:16]
