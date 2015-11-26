import holidays


def stat_holiday(province='BC', year=2015):
    """ Returns stat holidays dates for a given province and year. """
    return holidays.Canada(state=province, years=year).keys()
