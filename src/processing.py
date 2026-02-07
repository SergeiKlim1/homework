from datetime import datetime
from typing import List, Dict, Any


def filter_by_state(transactions: List[Dict[str, Any]], state = "EXECUTED") -> List[Dict[str, Any]]:
    """"
    Функция, которая принимает список словарей и опционально значение
    для ключа "state" (по умолчанию "EXECUTED") и возвращает новый список
    словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению
    """
    transactions_list = []

    for transaction in transactions:
        if transaction["state"] == state:
            transactions_list.append(transaction)

    return transactions_list

