from __future__ import absolute_import
import argparse
import datetime

from . import lexer
from . import rc


def setup_args():
    argp = argparse.ArgumentParser('Vacation Tracker')
    argp.add_argument('input', nargs='*', help='TODO')  # TODO: Write help text
    return argp.parse_args()


def main():
    args = setup_args()

    tokens = lexer.lex(args.input)
    rc.touch_rc()  # Make sure ~/.vacationrc exists
    rc.execute(tokens)

if __name__ == '__main__':
    main()
