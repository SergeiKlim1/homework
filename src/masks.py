def get_mask_card_number(card_number: str | int) -> str:
    """Функция, которая принимает и маскирует номер карты"""
    card_number_str = str(card_number)
    if len(card_number_str) == 16:
        mask_card = (
            card_number_str[0:6]
            + (len(card_number_str[6:-4]) * "*")
            + card_number_str[-4:]
        )
        mask_card_number = " ".join(
            [mask_card[i:i + 4] for i in range(0, len(mask_card), 4)]
        )
        return mask_card_number
    elif len(card_number_str) == 0:
        raise ValueError("Строка пустая")
    else:
        raise ValueError("Введены не корректные данные")


def get_mask_account(account_number: str | int) -> str:
    """Функция, которая принимает и маскирует номер счета"""
    account_number_str = str(account_number)
    if len(account_number_str) == 20:
        mask_account_number = account_number_str.replace(account_number_str[0:-4], "**")
        return mask_account_number
    elif len(account_number_str) == 0:
        raise ValueError("Строка пустая")
    else:
        raise ValueError("Введены не корректные данные")
