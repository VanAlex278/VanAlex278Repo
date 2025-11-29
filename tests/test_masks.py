import pytest

from src.masks import get_mask_account, get_mask_card_number, process_bank_search, process_bank_operations


@pytest.mark.parametrize("cart_number, cart_mask", [
    (7000792289606361, '7000 79** **** 6361'),
    (1596837868705199, '1596 83** **** 5199'),
    (75000792289606361, 'Некорректный номер карты'),
    ('7000792289606361', '7000 79** **** 6361'),
    ])
def test_get_mask_card_number(cart_number, cart_mask):
    assert get_mask_card_number(cart_number) == cart_mask


@pytest.mark.parametrize("account_number, account_mask", [
    (73654810843013574305, '**4305'),
    (736548108430135874, "Некорректный номер счета"),
    (35383033474447895560, '**5560'),
    ('73654108430135874505', '**4505'),
    ])
def test_get_mask_account(account_number, account_mask):
    assert get_mask_account(account_number) == account_mask


def test_process_bank_search(test_list_of_transactions):
    result = process_bank_search(test_list_of_transactions, "карты")
    assert result == [{
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
    }]

def test_process_bank_operations(test_list_of_transactions):
    result = str(process_bank_operations(test_list_of_transactions))
    assert result == "Counter({'Перевод организации': 2, 'Перевод со счета на счет': 2, 'Перевод с карты на карту': 1})"