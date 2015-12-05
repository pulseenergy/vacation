import os


def get_rc_path():
    """ Return the full .vacationrc path for convenience. """
    return os.path.join(os.path.expanduser('~'), '.vacationrc')


def touch():
    """ Create a .vacationrc file if none exists. """
    if not os.path.isfile(get_rc_path()):
        open(get_rc_path(), 'a').close()
        print('Created file: {}'.format(get_rc_path()))


def read():
    """ Read file and return entries as a list. """
    try:
        with open(get_rc_path(), 'r') as rc:
            return rc.readlines()
    except IOError:
        print('Error reading your ~/.vacationrc file!')
        return []


def write(entries):
    """ Write an entire rc file. """
    try:
        with open(get_rc_path(), 'w') as rc:
            rc.writelines(entries)
    except IOError:
        print('Error writing your ~/.vacationrc file!')


def validate():
    """ Before we execute any actions, let's validate our .vacationrc. """
    transactions = read()
    if not transactions:
        print('Your .vacationrc file is empty! Set days and rate.')
        return False
    return validate_setup(transactions)  # Validate the rate / days settings


def append(entry):
    """ Append either a list of strings or a string to our file. """
    if not entry:
        return
    try:
        with open(get_rc_path(), 'a') as f:
            if isinstance(entry, list):
                f.writelines(entry)
            else:
                f.write(entry + '\n')
    except IOError:
        print('Error writing your ~/.vacationrc file!')


def delete(bad_entry):
    """ Removes an entry from rc file. """
    entries = read()
    kept_entries = [x for x in entries if x.rstrip() != bad_entry]
    write(kept_entries)

