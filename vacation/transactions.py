"""
Sample vacation transaction file:

2015-11-08: days 10.5
2015-11-08: rate 1.333
2015-12-25: off
2015-12-26: off
2015-01-01: rate 1.5
2015-01-31: off

"""
import datetime

import holidays
import workdays


def validate_setup(transactions):
    """ First two transactions must set rate & days. """
    if not transactions:
        return True
    try:
        first, second = transactions[:2]
    except ValueError:
        print('Error: vacationrc file must have both initial days and rates entries')
        return False

    parts1, parts2 = first.split(), second.split()

    if parts1[0] != parts2[0]:
        print('Error: First two entries in vacationrc must have the same date')
        return False  # Dates must match

    if 'rate' not in (parts1[1], parts2[1]) or 'days' not in (parts1[1], parts2[1]):
        print('Error: First two entries in vacationrc must set days and rate')
        return False

    return True


def _parse_transaction_entry(entry):
    """ Validate & parse a transaction into (date, action, value) tuple. """
    parts = entry.split()

    date_string = parts[0]
    try:
        date = datetime.datetime.strptime(date_string[:-1], '%Y-%m-%d').date()
    except ValueError:
        raise ValueError('Invalid date in vacationrc for entry: {}'.format(entry))

    if len(parts) < 2:
        raise ValueError('.vacationrc missing an action for entry: {}'.format(entry))
    action = parts[1].lower()
    if action not in ('days', 'rate', 'off', 'adjust', 'show'):
        raise ValueError('Invalid action in vacationrc for entry: {}'.format(entry))

    try:
        value = float(parts[2])
    except IndexError:
        value = None
    except (ValueError, TypeError):
        raise ValueError('Invalid value in vacationrc for entry: {}'.format(entry))

    return (date, action, value)


def stat_holidays(province='BC', year=2015):
    """ Returns a list of holiday dates for a province and year. """
    return holidays.Canada(state=province, years=year).keys()


def sum_transactions(transactions):
    """ Sums transactions into a total of remaining vacation days. """
    workdays_per_year = 250
    last_date = None
    rate = 0
    day_sum = 0
    transactions.append('{}: show'.format(datetime.date.today().strftime('%Y-%m-%d')))
    for transaction in transactions:
        date, action, value = _parse_transaction_entry(transaction)

        if action == 'days':
            day_sum = value
        elif action == 'rate':
            rate = float(value) / workdays_per_year

        if last_date is None:
            last_date = date

        elapsed = workdays.networkdays(last_date, date, stat_holidays()) - 1
        if action == 'off':
            elapsed -= 1  # Didn't work that day
            day_sum -= 1  # And we used a day

        day_sum += rate * elapsed
        last_date = date

    return round(day_sum, 1)

