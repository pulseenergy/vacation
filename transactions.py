"""
Sample vacation transaction file:

2015-11-08: dates 10.5
2015-11-08: rate 1.333
2015-12-25: off
2015-12-26: off
2015-01-01: rate 1.5
2015-01-31: off

"""
from datetime import datetime


def validate_setup(transactions):
    """ First two transactions must be set rate or set dates. """
    if not transactions:
        return True
    try:
        first, second = transactions[:2]
    except IndexError:
        print('Error: vacationrc file must have both initial dates and rates entries')

    parts1, parts2 = first.split(), second.split()

    if parts1[0] != parts2[0]:
        print('Error: First two entries in vacationrc must have the same date')
        return False  # Dates must match

    if 'rate' not in (parts1[1], parts2[1]) or 'dates' not in (parts1[1], parts2[1]):
        print('Error: First two entries in vacationrc must set dates and rate')
        return False

    return True


def parse_transaction_entry(entry):
    """ Validate & parse a transaction into (date, action, value) tuple. """
    parts = entry.split()

    date_string = parts[0]
    try:
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError('Invalid date in vacationrc for entry: {}'.format(entry))

    if len(parts) < 2:
        raise ValueError('.vacationrc missing an action for entry: {}'.format(entry))
    action = parts[1].lower()
    if action not in ('dates', 'rate', 'off', 'adjust'):
        raise ValueError('Invalid action in vacationrc for entry: {}'.format(entry))

    try:
        value = float(parts[2])
    except IndexError:
        value = None
    except (ValueError, TypeError):
        raise ValueError('Invalid value in vacationrc for entry: {}'.format(entry))

    return (date, action, value)
