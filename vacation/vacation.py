import argparse

import parser


def setup_args():
    parser = argparse.ArgumentParser('Vacation Tracker')
    parser.add_argument('input', nargs='*')
    return parser.parse_args()


def main():
    args = setup_args()
    print('Input args: {}'.format(args.input))

    def tester():
        print(args)
    tester()
    parser.parse(args.input)

    print("5 vacation days remaining")


def test():
    print("testing")


if __name__ == '__main__':
    main()
