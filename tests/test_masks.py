import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def account_number():
    return "73654108430135874305"


@pytest.fixture
def card_number():
    return "7000792289606361"


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == "**4305"
