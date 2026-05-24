from typing import Dict, List, Any, Generator


def filter_by_currency(list_dict: List [Dict[str, Any]], currency: str) -> Generator[List[dict, Any], None, None]:

    """Функция возвращающая итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""


    filtered_list_dict = (transaction for transaction in list_dict if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency)
    return filtered_list_dict


def transaction_descriptions(list_dict: List [Dict[str, Any]]) -> Generator[str, None, None]:

    """Генератор, который принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""


    for transaction in list_dict:
        description = transaction.get("description", "")
        yield description

