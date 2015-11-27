import datetime

from nose.tools import assert_almost_equals

from vacation import transactions as trans

transactions = [
    '2015-11-01: days 0',
    '2015-11-01: rate 20',
    '2015-11-10: off',
    '2015-11-15: show',
]


def test_validate_setup_empty():
    assert trans.validate_setup([]) is True


def test_validate_setup_missing_rate():
    assert trans.validate_setup(transactions[:1]) is False


def test_validate_setup_good():
    assert trans.validate_setup(transactions) is True


def test_validate_setup_bad_dates():
    bad = transactions.copy()
    bad[0] = '2015-11-02: days 0'  # Wrong date
    print(bad)
    assert trans.validate_setup(bad) is False


def test_validate_setup_bad_missing_set():
    bad = transactions.copy()
    del bad[1]  # Missing rate
    assert trans.validate_setup(bad) is False


def test_parse_transaction_entry_good_value():
    entry = transactions[1]
    expected = (datetime.date(2015, 11, 1), 'rate', 20.0)
    assert trans._parse_transaction_entry(entry) == expected


def test_parse_transaction_entry_good_no_value():
    entry = transactions[2]
    expected = (datetime.date(2015, 11, 10), 'off', None)
    assert trans._parse_transaction_entry(entry) == expected


def test_sum_transactions_easy():
    result = trans.sum_transactions(transactions)
    expected = 15 * (20.0 / 250) - 1
    assert_almost_equals(result, expected)

