
SHOW = 'show'
TAKE = 'take'
TAKERANGE = 'takerange'
SETRATE = 'setrate'
SETDAYS = 'setdays'
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def lex(args):
    """ Lex input. """
    if len(args) == 0:
        return [(SHOW)]
    elif isMonth(args[0]):
        if not args[2:]:
            return [(TAKE, lexDate(args[0:2]))]


def lexDate(args):
    #print('\n@@@ {}'.format(args))
    month = args[0][:3].lower()
    day = int(args[1])
    if not isMonth(args[0]):
        raise ValueError('Not valid month')
    return '{} {}'.format(month, day)

def isMonth(arg):
    month = arg[:3].lower()
    return month in MONTHS
