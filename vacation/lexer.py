SHOW = 'show'
TAKE = 'take'
SET = 'set'
RATE = 'rate'
DAYS = 'days'
TAKERANGE = 'takerange'
SETRATE = 'setrate'
SETDAYS = 'setdays'
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def lex(args):
    """ Lex input. """
    if len(args) == 0:
        return [(SHOW,)]
    elif args[0] == SHOW:
        return [(SHOW,)]
    elif args[0] == SET and args[1] == RATE:
        return tokenizeSetRate(args[2:])
    elif args[0] == SET and args[1] == DAYS:
        return tokenizeSetDays(args[2:])
    elif isMonth(args[0]):
        return tokenizeTake(args)

def tokenizeSetRate(args):
    if not args[0:]:
        raise ValueError('Missing args for <set rate>')
    try:
        rate = float(args[0])
    except ValueError:
        raise ValueError('Invalid rate: {}'.format(args))
    return [(SETRATE, '{}'.format(rate))]

def tokenizeSetDays(args):
    if not args[0:]:
        raise ValueError('Missing args for <set days>')
    try:
        days = float(args[0])
    except ValueError:
        raise ValueError('Invalid number of days: {}'.format(args))
    return [(SETDAYS, '{}'.format(days))]

def tokenizeTake(args):
    ret = [(TAKE, date) for date in lexDate(args)]
    return ret

def isMonth(arg):
    month = arg[:3].lower()
    return month in MONTHS

def lexDate(args):
    month = args[0][:3].lower()
    if not isMonth(args[0]):
        raise ValueError('Not a valid month')
    dates = []
    for arg in args[1:]:
        day = getDay(arg)
        dates.append('{} {}'.format(month, day))
    return dates

def getDay(arg):
    arg = arg.strip(',')
    try:
        return int(arg)
    except ValueError:
        raise ValueError('Invalid day: {}'.format(arg))
