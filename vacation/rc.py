import os


def rc_file():
    """ Return the full .vacationrc path for convenience. """
    return os.path.join(os.path.expanduser('~'), '.vacationrc')


def touch_rc(rc_file):
    """ Create a .vacationrc file if none exists. """
    if not os.path.isfile(rc_file):
        open(rc_file, 'a').close()


def read_rc(rc_file):
    """ Read RC file and return entries as a list. """
    try:
        with open(rc_file, 'r') as rc:
            return rc.readlines()
    except IOError:
        print('Error reading your ~/.vacationrc file!')
        return []


def append_rc(rc_file, entry):
    """ Append either a list of strings or a string to our RC file. """
    if not entry:
        return
    try:
        with open(rc_file, 'a') as rc:
            if isinstance(entry, list):
                rc.writelines(entry)
            else:
                rc.write(entry + '\n')
    except IOError:
        print('Error reading your ~/.vacationrc file!')
