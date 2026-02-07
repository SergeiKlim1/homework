from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая принимает имя карты или счет и маскирует маску карты или счета"""
    name_card = account_card[0:-len(account_card.split()[-1])]
    number_account_card = account_card.split()[-1]
    if len(account_card.split()[-1]) == 16:
        mask_account = name_card + get_mask_card_number(number_account_card)
    else:
        mask_account = name_card + get_mask_account(number_account_card)
    return mask_account


def get_date(date: str) -> str:
    """Функция, которая принимает дату в iso формате и возвращает дату в формате дд.мм.гггг"""
    date_iso = datetime.fromisoformat(date)
    new_date = datetime.strftime(date_iso, "%d.%m.%Y")
    return new_date
