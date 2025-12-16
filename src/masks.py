def get_mask_card_number(card_number: int) -> str:
    """Функция, которая принимает и маскирует номер карты"""
    card_number_string = str(card_number)
    mask_card = (
        card_number_string[0:6]
        + (len(card_number_string[6:-4]) * "*")
        + card_number_string[-4:]
    )
    mask_card_number = " ".join(
        [mask_card[i:i + 4] for i in range(0, len(mask_card), 4)]
    )
    return mask_card_number


def get_mask_account(account_number: int) -> str:
    """Функция, которая принимает и маскирует номер счета"""
    string_account_number = str(account_number)
    mask_account_number = string_account_number.replace(
        string_account_number[0:-4], "**"
    )
    return mask_account_number
