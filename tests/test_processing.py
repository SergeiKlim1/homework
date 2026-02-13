import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def transactions():
    return [
        {'id': 414288290, '': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 600719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, '': 'CANCELED', 'date': '2018-10-01T21:27:25.241689'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
    ]

@pytest.mark.parametrize("state, expected", [
                         ('EXECUTED', [{'id': 600719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                         ('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}])])

def test_filter_by_state(state, expected, transactions):
    assert filter_by_state(transactions, state=state) == expected


@pytest.mark.parametrize("type_sort, expected",
                         [(True, [{'id': 414288290, '': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                 {'id': 594226727, '': 'CANCELED', 'date': '2018-10-01T21:27:25.241689'},
                                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                  {'id': 600719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                         (False, [{'id': 600719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                  {'id': 594226727, '': 'CANCELED', 'date': '2018-10-01T21:27:25.241689'},
                                  {'id': 414288290, '': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])]
                         )
def test_sort_by_date(type_sort, expected, transactions):
    assert sort_by_date(transactions, type_sort) == expected


@pytest.mark.parametrize("transaction_with_incorrect_date, expected",
                         [([{'id': 414288290, 'state': 'EXECUTED', 'date': '03.07.2019'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': ''}], "Дата не в iso формате")])
def test_sort_by_incorrect_date(transaction_with_incorrect_date, expected):
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(transaction_with_incorrect_date)
    assert str(exc_info.value) == expected