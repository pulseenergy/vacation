import argparse

import lexer


def setup_args():
    argp = argparse.ArgumentParser('Vacation Tracker')
    argp.add_argument('input', nargs='*')
    return argp.parse_args()


def main():
    args = setup_args()
    print('Input args: {}'.format(args.input))

    def tester():
        print(args)
    tester()
    tokens = lexer.lex(args.input)

    print("5 vacation days remaining")


def test():
    print("testing")


if __name__ == '__main__':
    main()
