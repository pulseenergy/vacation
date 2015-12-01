from __future__ import absolute_import
import argparse

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
    rc.execute(tokens)
    trans = rc.read_rc()  # Read transactions

    if not trans:
        print('Your .vacationrc file is empty! Set days and rate.')
    else:
        if transactions.validate_setup(trans):  # Validate
            # TODO: We might want to show in the future, or in the past
            trans.append('{}: show'.format(datetime.date.today().strftime('%Y-%m-%d')))
            days_remaining = transactions.sum_transactions(trans)  # sum up our new days remaining
            print('{} vacation days remaining'.format(days_remaining))


if __name__ == '__main__':
    main()
