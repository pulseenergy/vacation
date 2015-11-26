import datetime

import transactions as trans

transactions = [
    '2015-11-01: dates 0',
    '2015-11-01: rate 0.5',
    '2015-11-30: off',
    '2015-12-25: off',
]


def test_validate_setup_empty():
    assert trans.validate_setup([]) is True


def test_validate_setup_good():
    assert trans.validate_setup(transactions) is True


def test_validate_setup_bad_dates():
    bad = transactions.copy()
    bad[0] = '2015-11-02: dates 0'  # Wrong date
    print(bad)
    assert trans.validate_setup(bad) is False


def test_validate_setup_bad_missing_set():
    bad = transactions.copy()
    del bad[1]  # Missing rate
    assert trans.validate_setup(bad) is False


def test_parse_transaction_entry_good_value():
    entry = transactions[1]
    expected = (datetime.date(2015, 11, 1), 'rate', 0.5)
    assert trans.parse_transaction_entry(entry) == expected


def test_parse_transaction_entry_good_no_value():
    entry = transactions[2]
    expected = (datetime.date(2015, 11, 30), 'off', None)
    assert trans.parse_transaction_entry(entry) == expected

