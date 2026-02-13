from datetime import datetime
from typing import List, Dict, Any


def filter_by_state(
    transactions: List[Dict[str, Any]], state="EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Функция, которая принимает список словарей и опционально значение
    для ключа "state" (по умолчанию "EXECUTED") и возвращает новый список
    словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению
    """
    transactions_list_with_state = []
    transactions_list = []


    for transaction in transactions:
        for key in transaction:
            if key == "state":
                transactions_list_with_state.append(transaction)

    for transaction in transactions_list_with_state:
        if transaction["state"] == state:
            transactions_list.append(transaction)
    return transactions_list


def sort_by_date(
    transactions: List[Dict[str, Any]], type_sort=True
) -> List[Dict[str, Any]]:
    """
    Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание) и возвращает
    новый список отсортированный по дате
    """
    try:
        sorted_list_by_date = sorted(
        transactions,
        key=lambda x: (datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), x["id"]),
        reverse=type_sort)
        return sorted_list_by_date
    except ValueError:
        raise ValueError("Дата не в iso формате")


