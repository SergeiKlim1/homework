import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "names, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(names, expected):
    assert mask_account_card(names) == expected


@pytest.mark.parametrize(
    "incorrect_names, expected",
    [
        ("Счет 1596837868705199", "Введены не корректные данные"),
        ("", "Строка пустая"),
        ([], "Введены не корректные данные"),
        ("Счет 3538303347444789550", "Введены не корректные данные"),
    ],
)
def test_mask_incorrect_account_card(incorrect_names, expected):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(incorrect_names)
    assert str(exc_info.value) == expected


@pytest.fixture()
def date_example():
    return "2024-03-11T02:26:18.671407"


def test_get_date(date_example):
    assert get_date(date_example) == "11.03.2024"


@pytest.mark.parametrize(
    "incorrect_date, expected",
    [
        ("", "Строка пустая"),
        ("11.02.2004", "Дата не соответствует iso формату"),
        ("21/10/04", "Дата не соответствует iso формату"),
    ],
)
def test_get_incorrect_date(incorrect_date, expected):
    with pytest.raises(ValueError) as exc_info:
        get_date(incorrect_date)
        assert str(exc_info.value) == expected
