from typing import List, Any, Generator


def filter_by_currency(list_dict: List [dict, any], currency: str) -> Generator[List[dict, Any], None, None]:

    """"Функция возвращающая итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""


    filtered_list_dict = (transaction for transaction in list_dict if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency)
    return filtered_list_dict

