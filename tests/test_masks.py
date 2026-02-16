import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        (1596837868705199, "1596 83** **** 5199"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "incorrect_number, expected",
    [
        ("", "Строка пустая"),
        ("fhd", "Введены не корректные данные"),
        ({}, "Введены не корректные данные"),
    ],
)
def test_get_mask_incorrect_card_number(incorrect_number, expected):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(incorrect_number)
    assert str(exc_info.value) == expected


@pytest.mark.parametrize(
    "incorrect_number, expected",
    [
        ("", "Строка пустая"),
        ("fhd", "Введены не корректные данные"),
        ([], "Введены не корректные данные"),
    ],
)
def test_get_mask_incorrect_account(incorrect_number, expected):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(incorrect_number)
    assert str(exc_info.value) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
