import pdb

SHOW = 'show'
TAKE = 'take'
TAKERANGE = 'takerange'
SETRATE = 'setrate'
SETDAYS = 'setdays'
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def lex(args):
    """ Lex input. """
    if len(args) == 0:
        # Show user their vacation days
        return [(SHOW)]
    elif isMonth(args[0]):
        # Take one vacation day
        ret = [(TAKE, date) for date in lexDate(args[0:])]
        #print('\n@@@ {}'.format(ret))
        return ret


def lexDate(args):
    month = args[0][:3].lower()
    if not isMonth(args[0]):
        raise ValueError('Not valid month')

    dates = []
    for arg in args[1:]:
        day = getDay(arg)
        dates.append('{} {}'.format(month, day))

    return dates

def isMonth(arg):
    month = arg[:3].lower()
    return month in MONTHS

def getDay(arg):
    arg = arg.strip(',')
    try:
        return int(arg)
    except ValueError:
        raise ValueError('Invalid day: {}'.format(arg))
