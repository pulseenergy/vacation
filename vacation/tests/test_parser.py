import parser


def test_no_args():
    inputs = []
    expected = [('yield',)]
    assert parser.parse(inputs) == expected

def test_one_date():
    inputs = ['Nov', '8']
    expected = [('yield',)]
    assert parser.parse(inputs) == expected

def test_two_dates():
    inputs = ['Nov', '8,', '12']
    expected = [('yield',)]
    assert parser.parse(inputs) == expected

def test_date_easy_range():
    inputs = ['Nov', '8-10']
    expected = [('yield',)]
    assert parser.parse(inputs) == expected

def test_date_months_range():
    inputs = ['Nov', '8', '-', 'Dec', '2']
    expected = [('yield',)]
    assert parser.parse(inputs) == expected

def test_date_months_range_sub():
    inputs = ['Nov', '8-Dec', 'Dec', '2']
    expected = [('yield',)]
    assert parser.parse(inputs) == expected

def test_date_crazy():
    inputs = ['Nov30-Dec2']
    expected = [('yield',)]
    assert parser.parse(inputs) == expected

def test_set_rate():
    inputs = ['set', 'rate', '1.333']
    expected = [('yield',)]
    assert parser.parse(inputs) == expected

def test_set_days():
    inputs = ['set', 'days', '10.5']
    expected = [('yield',)]
    assert parser.parse(inputs) == expected

