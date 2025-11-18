import os

import requests
from dotenv import load_dotenv


def currency_conversion(list_transaction: list) -> float:
    """Функция конвертации валюты из USD и EUR в рубли, возвращает сумму транзакции в рублях."""
    amount = float(list_transaction["operationAmount"]["amount"])
    from_currency = list_transaction["operationAmount"]["currency"]["code"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_currency}&amount={amount}"
    payload = {}
    load_dotenv()
    headers = {"apikey": os.getenv("APILAYER_API_KEY")}
    try:
        response = requests.get(url, headers=headers, data=payload)
    except requests.exceptions.ConnectionError:
        print("Connection Error. Please check your network connection.")
    status_code = response.status_code
    result = response.json()
    if status_code == 200:
        amount_rub = float(result["result"])
        return amount_rub
    else:
        return status_code
