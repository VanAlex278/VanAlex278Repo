import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "start, stop, first, second",
    [
        (1, 5, "0000 0000 0000 0001", "0000 0000 0000 0002"),
        (1000000000000000, 1000000000000005, "1000 0000 0000 0000", "1000 0000 0000 0001"),
    ],
)
def test_card_number_generator(start, stop, first, second):
    gen = card_number_generator(start, stop)
    assert next(gen) == first
    assert next(gen) == second


def test_filter_by_currency(test_list_of_transactions):
    one_transaction = filter_by_currency(test_list_of_transactions)
    assert next(one_transaction) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_usd(test_list_of_transactions):
    one_transaction = filter_by_currency(test_list_of_transactions, "USD")
    assert next(one_transaction) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_transaction_descriptions(test_list_of_transactions):
    one_transaction = transaction_descriptions(test_list_of_transactions)
    assert next(one_transaction) == "Перевод организации"
