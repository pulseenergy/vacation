from vacation import lexer


def test_no_args():
    inputs = []
    expected = [('show', None)]
    assert lexer.lex(inputs) == expected

def test_one_date():
    inputs = ['Nov', '8']
    expected = [('take', 'nov 8')]
    assert lexer.lex(inputs) == expected

def test_two_dates():
    inputs = ['Nov', '8,', '12']
    expected = [('take', 'nov 8'), ('take', 'nov 12')]
    assert lexer.lex(inputs) == expected

def test_take_one_date():
    inputs = ['take', 'Nov', '8']
    expected = [('take', 'nov 8')]
    assert lexer.lex(inputs) == expected

def test_take_two_dates():
    inputs = ['take', 'Nov', '8,', '12']
    expected = [('take', 'nov 8'), ('take', 'nov 12')]
    assert lexer.lex(inputs) == expected

# def test_date_easy_range():
#     inputs = ['Nov', '8-10']
#     expected = [('takerange', 'nov 8', 'nov 10')]
#     assert lexer.lex(inputs) == expected
#
# def test_date_months_range():
#     inputs = ['Nov', '8', '-', 'Dec', '2']
#     expected = [('takerange', 'nov 8', 'dec 2')]
#     assert lexer.lex(inputs) == expected
#
# def test_date_months_range_sub():
#     inputs = ['Nov', '8-Dec', 'Dec', '2']
#     expected = [('takerange', 'nov 8', 'dec 2')]
#     assert lexer.lex(inputs) == expected
#
# def test_date_crazy():
#     inputs = ['Nov30-Dec2']
#     expected = [('takerange', 'nov 30', 'dec 2')]
#     assert lexer.lex(inputs) == expected

def test_set_rate():
    inputs = ['set', 'rate', '1.333']
    expected = [('setrate', '1.333')]
    assert lexer.lex(inputs) == expected

def test_set_days():
    inputs = ['set', 'days', '10.5']
    expected = [('setdays', '10.5')]
    assert lexer.lex(inputs) == expected

# def test_manually_add_day():
#     inputs = ['adjust', '+1']
#     expected = [('adjust', '1')]
#     assert lexer.lex(inputs) == expected
#
# def test_manually_subtract_day():
#     inputs = ['adjust', '-1']
#     expected = [('adjust', '-1')]
#     assert lexer.lex(inputs) == expected
