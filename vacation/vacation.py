import argparse
import datetime

import lexer
import transactions
import rc


def setup_args():
    argp = argparse.ArgumentParser('Vacation Tracker')
    argp.add_argument('input', nargs='*', help='TODO')  # TODO: Write help text
    return argp.parse_args()


def main():
    args = setup_args()

    rc_file = rc.rc_file()  # transaction file name

    tokens = lexer.lex(args.input)
    for token in tokens:
        if token[0] == 'show':
            break
        if token[0] == 'take':
            date_str = token[1] + '-{}'.format(datetime.date.today().year)

            date = datetime.datetime.strptime(date_str, '%b %d-%Y').date()
            rc.append_rc(rc_file, '{}: off'.format(date.strftime('%Y-%m-%d')))

    trans = rc.read_rc(rc_file)  # Read transactions
    transactions.validate_setup(trans)  # Validate
    days_remaining = transactions.sum_transactions(trans)  # sum up our new days remaining

    print('{} vacation days remaining'.format(days_remaining))


def test():
    print("testing")


if __name__ == '__main__':
    main()
