import pytest

from src.masks import get_mask_account, get_mask_card_number


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
