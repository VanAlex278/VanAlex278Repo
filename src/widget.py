from masks import get_mask_account, get_mask_card_number


def \
        mask_account_card(card_account_number: str) -> str:
    """Функцию маскировки номера банковской карты или номера счета"""
    list_cart_account = card_account_number.split(" ")
    if len(list_cart_account[-1]) == 16:
        list_cart_account[-1] = get_mask_card_number(list_cart_account[-1])
    elif len(list_cart_account[-1]) == 20:
        list_cart_account[-1] = get_mask_account(list_cart_account[-1])
    else:
        return "Некорректный ввод данных"
    return " ".join(list_cart_account)


def get_date(old_data: str) -> str:
    """Возвращает дату в формате "ДД.ММ.ГГГГ" """
    return old_data[8:10] + "." + old_data[5:7] + "." + old_data[:4]
