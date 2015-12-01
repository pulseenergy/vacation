import datetime

from nose.tools import assert_almost_equals

from vacation import transactions as trans


def test_validate_setup_empty():
    assert trans.validate_setup([]) is True


def test_validate_setup_missing_rate():
    transactions = ['2015-11-01: days 0']
    assert trans.validate_setup(transactions[:1]) is False


def test_validate_setup_good():
    transactions = [
        '2015-11-01: days 0',
        '2015-11-01: rate 20',
        '2015-11-10: off',
        '2015-11-15: show',
    ]
    assert trans.validate_setup(transactions) is True


def test_validate_setup_bad_dates():
    transactions = [
        '2015-11-02: days 0',  # Wrong date
        '2015-11-01: rate 20',
        '2015-11-10: off',
        '2015-11-15: show',
    ]
    assert trans.validate_setup(bad) is False


def test_validate_setup_bad_missing_set():
    transactions = [  # Missing set rate
        '2015-11-01: days 0',
        '2015-11-10: off',
        '2015-11-15: show',
    ]
    assert trans.validate_setup(bad) is False


def test_parse_transaction_entry_good_value():
    entry = '2015-11-01: rate 20'
    expected = (datetime.date(2015, 11, 1), 'rate', 20.0)
    assert trans._parse_transaction_entry(entry) == expected


def test_parse_transaction_entry_good_no_value():
    entry = '2015-11-10: off'
    expected = (datetime.date(2015, 11, 10), 'off', None)
    assert trans._parse_transaction_entry(entry) == expected


def test_sum_transactions_easy():
    transactions = [  # 8 working days: 10 off & 11 is Holiday
        '2015-11-01: days 0',
        '2015-11-01: rate 20',
        '2015-11-15: show',
    ]
    expected = 8 * (20.0 / 250)
    assert_almost_equals(trans.sum_transactions(transactions), expected)


def test_sum_transactions_set_days():
    transactions = [
        '2015-11-01: days 0',
        '2015-11-01: rate 20',
        '2015-11-10: off',
        '2015-11-15: days 7',
    ]
    assert_almost_equals(trans.sum_transactions(transactions), 7)

