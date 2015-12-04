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


def write_rc(entries):
    """ Write an entire rc file. """
    try:
        with open(rc_file(), 'w') as rc:
            rc.writelines(entries)
    except IOError:
        print('Error writing your ~/.vacationrc file!')


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


def delete_rc(bad_entry):
    """ Removes an entry from rc file. """
    entries = read_rc()
    kept_entries = [x for x in entries if x.rstrip() != bad_entry]
    write_rc(kept_entries)

