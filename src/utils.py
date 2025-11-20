import json
import logging
from json import JSONDecodeError


logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def list_transaction_returned(path_to_json_file: str = "../data/operations.json") -> list[dict]:
    """Функция чтения JSON-файла возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path_to_json_file, encoding="utf-8") as f:
            list_transaction = json.load(f)
            logger.info(f'Load file: {path_to_json_file}')
            if list_transaction is None:
                logger.warning(f'file: {path_to_json_file} unsupported format')
                return []
            elif type(list_transaction) is not list:
                logger.warning(f'file: {path_to_json_file} unsupported format')
                return []
        return list_transaction
    except (FileNotFoundError, JSONDecodeError) as e:
        logger.error(f"The file is missing or corrupted! {e}")
        return []
