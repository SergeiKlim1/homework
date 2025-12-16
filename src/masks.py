def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает и маскирует номер карты"""
    mask_card = (
        card_number[0:6]
        + (len(card_number[6:-4]) * "*")
        + card_number[-4:]
    )
    mask_card_number = " ".join(
        [mask_card[i:i + 4] for i in range(0, len(mask_card), 4)]
    )
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает и маскирует номер счета"""
    mask_account_number = account_number.replace(
        account_number[0:-4], "**"
    )
    return mask_account_number
