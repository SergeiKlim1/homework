from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая принимает номер, имя карты или счет и выводит в замаскированном виде"""
    account_card_str = str(account_card)
    if len(account_card_str) == 0:
        raise ValueError("Строка пустая")
    else:
        name_card = account_card_str[0:-len(account_card_str.split()[-1])]
        number_account_card = account_card_str.split()[-1]
        if len(number_account_card) == 16 and name_card != "Счет ":
            mask_account = name_card + get_mask_card_number(number_account_card)
            return mask_account
        elif len(number_account_card) == 20 and name_card == "Счет ":
            mask_account = name_card + get_mask_account(number_account_card)
            return mask_account
        else:
            raise ValueError("Введены не корректные данные")


def get_date(date: str) -> str:
    """Функция, которая принимает дату в iso формате и возвращает в формате дд.мм.гггг"""
    date_str = str(date)
    if date_str == "":
        raise ValueError("Строка пустая")
    else:
        try:
            new_date = datetime.strftime(datetime.fromisoformat(date_str), "%d.%m.%Y")
            return new_date
        except ValueError:
            raise ValueError("Дата не соответствует iso формату")
