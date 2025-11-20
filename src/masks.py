import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Функцию маскировки номера банковской карты"""
    card_number1 = str(card_number)
    if len(card_number1) != 16 or not card_number1.isdigit():
        logger.warning(f'{card_number} wrong')
        return "Некорректный номер карты"
    card_mask = card_number1[:4] + " " + card_number1[4:6] + "** **** " + card_number1[-4:]
    logger.info(f'mask_card: {card_mask}')
    return card_mask


def get_mask_account(account_number: int) -> str:
    """Функцию маскировки номера банковского счета"""
    account_number1 = str(account_number)
    if len(account_number1) != 20 or not account_number1.isdigit():
        logger.warning(f'{account_number} wrong')
        return "Некорректный номер счета"
    account_mask = "**" + account_number1[-4:]
    logger.info(f'mask_account: {account_mask}')
    return account_mask
