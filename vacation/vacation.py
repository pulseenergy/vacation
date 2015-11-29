from __future__ import absolute_import

import argparse
import datetime

from . import lexer
from . import transactions
from . import rc


def setup_args():
    argp = argparse.ArgumentParser('Vacation Tracker')
    argp.add_argument('input', nargs='*', help='TODO')  # TODO: Write help text
    return argp.parse_args()


def main():
    args = setup_args()

    rc.touch_rc()  # Make sure ~/.vacationrc exists

    tokens = lexer.lex(args.input)
    for token in tokens:
        action = token[0]
        if action == 'show':
            break
        elif action == 'take':
            date_str = token[1] + '-{}'.format(datetime.date.today().year)
            date = datetime.datetime.strptime(date_str, '%b %d-%Y').date()
            rc.append_rc('{}: off'.format(date.strftime('%Y-%m-%d')))
        elif action == 'setrate':
            date = datetime.date.today()
            rc.append_rc('{}: rate {}'.format(date.strftime('%Y-%m-%d'), token[1]))
        elif action == 'setdays':
            date = datetime.date.today()
            rc.append_rc('{}: days {}'.format(date.strftime('%Y-%m-%d'), token[1]))

    trans = rc.read_rc()  # Read transactions
    if not trans:
        print('Your .vacationrc file is empty! Set days and rate.')
    else:
        if transactions.validate_setup(trans):  # Validate
            days_remaining = transactions.sum_transactions(trans)  # sum up our new days remaining
            print('{} vacation days remaining'.format(days_remaining))


if __name__ == '__main__':
    main()
