def get_mask_card_number(card_number: int) -> str:
    """Функцию маскировки номера банковской карты"""
    card_number1 = str(card_number)
    if len(card_number1) != 16 or not card_number1.isdigit():
        return "Некорректный номер карты"
    card_mask = card_number1[:4] + " " + card_number1[4:6] + "** **** " + card_number1[-4:]
    return card_mask


def get_mask_account(account_number: int) -> str:
    """Функцию маскировки номера банковского счета"""
    account_number1 = str(account_number)
    if len(account_number1) != 20 or not account_number1.isdigit():
        return "Некорректный номер счета"
    account_mask = "**" + account_number1[-4:]
    return account_mask
