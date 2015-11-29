import datetime
import os


def rc_file():
    """ Return the full .vacationrc path for convenience. """
    return os.path.join(os.path.expanduser('~'), '.vacationrc')


def touch_rc():
    """ Create a .vacationrc file if none exists. """
    if not os.path.isfile(rc_file()):
        open(rc_file(), 'a').close()
        print('Created file: {}'.format(rc_file()))


def read_rc():
    """ Read file and return entries as a list. """
    try:
        with open(rc_file(), 'r') as rc:
            return rc.readlines()
    except IOError:
        print('Error reading your ~/.vacationrc file!')
        return []


def append_rc(entry):
    """ Append either a list of strings or a string to our file. """
    if not entry:
        return
    try:
        with open(rc_file(), 'a') as f:
            if isinstance(entry, list):
                f.writelines(entry)
            else:
                f.write(entry + '\n')
    except IOError:
        print('Error writing your ~/.vacationrc file!')


def execute(tokens):
    """ Perform the actions described by the input tokens. """
    for token in tokens:
        action = token[0]
        if action == 'show':
            continue  # No need to do anything to our rc file
        elif action == 'take':
            date_str = token[1] + '-{}'.format(datetime.date.today().year)
            date = datetime.datetime.strptime(date_str, '%b %d-%Y').date()
            append_rc('{}: off'.format(date.strftime('%Y-%m-%d')))
        elif action == 'setrate':
            date = datetime.date.today()
            append_rc('{}: rate {}'.format(date.strftime('%Y-%m-%d'), token[1]))
        elif action == 'setdays':
            date = datetime.date.today()
            append_rc('{}: days {}'.format(date.strftime('%Y-%m-%d'), token[1]))

