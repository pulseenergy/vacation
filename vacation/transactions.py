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

from . import rc


def execute(tokens):
    """ Perform the actions described by the input tokens. """
    for action, value in tokens:
        if action == 'show':
            show()
        elif action == 'log':
            log_vacation_days()
        elif action == 'echo':
            echo_vacation_rc()
        elif action == 'take':
            take(value)
        elif action == 'cancel':
            cancel(value)
        elif action == 'setrate':
            setrate(value)
        elif action == 'setdays':
            setdays(value)


def show():
    trans = rc.read_rc()  # Read transactions

    # TODO-NTR: This code needs to be run before certain commands so some rethinking will be required
    if not trans:
        print('Your .vacationrc file is empty! Set days and rate.')
    else:
        if validate_setup(trans):  # Validate
            # TODO: We might want to show in the future, or in the past
            trans.append('{}: show'.format(datetime.date.today().strftime('%Y-%m-%d')))
            days_remaining = sum_transactions(trans)  # sum up our new days remaining
            print('{} vacation days remaining'.format(days_remaining))


def take(value, date=None):
    date_str = value + '-{}'.format(datetime.date.today().year)
    date = datetime.datetime.strptime(date_str, '%b %d-%Y').date()
    entry = '{}: off'.format(date.strftime('%Y-%m-%d'))
    rc.append_rc(entry)


def cancel(value, date=None):
    date_str = value + '-{}'.format(datetime.date.today().year)
    date = datetime.datetime.strptime(date_str, '%b %d-%Y').date()
    entry = '{}: off'.format(date.strftime('%Y-%m-%d'))
    rc.delete_rc(entry)

def setrate(value, date=None):
    date = datetime.date.today() if date is None else date
    entry = '{}: rate'.format(date.strftime('%Y-%m-%d'), value)
    rc.append_rc(entry)


def setdays(value, date=None):
    date = datetime.date.today() if date is None else date
    entry = '{}: days {}'.format(date.strftime('%Y-%m-%d'), value)
    rc.append_rc(entry)


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
    previous_date = None
    rate = 0
    day_sum = 0
    for transaction in transactions:
        date, action, value = _parse_transaction_entry(transaction)
        if previous_date is None:
            previous_date = date
        elapsed = workdays.networkdays(previous_date, date, stat_holidays()) - 1

        if action == 'rate':
            rate = float(value) / workdays_per_year
        elif action == 'off':
            elapsed -= 1  # Didn't work that day
            day_sum -= 1  # And we used a day
        day_sum += rate * elapsed

        if action == 'days':
            day_sum = value  # Fixed value as of this entry

        previous_date = date

    return day_sum


def get_days_off(transactions):
    """ Return the dates for any 'take day off' transactions. """
    days_off = []
    for trans in transactions:
        date, action, _ = _parse_transaction_entry(trans)
        if action == 'off':
            days_off.append(date)
    return days_off


def log_vacation_days():
    """ Sum and report taken days off. """
    days_off = get_days_off(rc.read_rc())
    pretty_days = map(lambda day: day.strftime('%a %b %d %Y'), days_off)
    for day in pretty_days:
        print(day)


def echo_vacation_rc():
    """ Display all our .vacationrc file. """
    contents = rc.read_rc()
    print('.vacationrc\n===========')
    for line in contents:
        print(line.rstrip())
