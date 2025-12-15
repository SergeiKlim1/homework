from masks import *


def mask_account_card(account_card: str) -> str:
    """"Функция, которая зозвращает имя карты или счет и маску карты или счета"""
    name_card = account_card[0:-len(account_card.split()[-1])]
    if len(account_card.split()[-1]) == 16:
        mask_account = name_card + get_mask_card_number(int(account_card.split()[-1]))
    else:
        mask_account = name_card + get_mask_account(int(account_card.split()[-1]))
    return mask_account


from datetime import datetime
def get_date(date: str) -> str:
    """"Функция, которая принимает дату в iso формате и возвращаяе дату в формате дд.мм.гггг"""
    date_iso = datetime.fromisoformat(date)
    new_date = datetime.strftime(date_iso,"%d.%m.%Y")
    return new_date

