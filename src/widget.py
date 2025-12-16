from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая принимает имя карты или счет и маскирует маску карты или счета"""
    name_card = account_card[0:-len(account_card.split()[-1])]
    number_account_card = int(account_card.split()[-1])
    if len(account_card.split()[-1]) == 16:
        mask_account = name_card + get_mask_card_number(number_account_card)
    else:
        mask_account = name_card + get_mask_account(number_account_card)
    return mask_account


def get_date(date: str) -> str:
    """Функция, которая принимает дату в iso формате и возвращаяе дату в формате дд.мм.гггг"""
    date_iso = datetime.fromisoformat(date)
    new_date = datetime.strftime(date_iso, "%d.%m.%Y")
    return new_date


if __name__ == "__main__":
    test1 = "MasterCard 7158300734726758"
    test2 = "Счет 64686473678894779589"
    test3 = "2024-03-11T02:26:18.671407"
    test4 = "Visa Classic 6831982476737658"

    print(mask_account_card(test1))
    print(mask_account_card(test2))
    print(get_date(test3))
    print(mask_account_card(test4))
