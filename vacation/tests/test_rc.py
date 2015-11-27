import os
from unittest.mock import Mock

from vacation import rc


def test_rc_file():
    temp = os.path.join(os.path.expanduser('~'), '.vacationrc')
    assert rc.rc_file() == temp


def test_touch_rc():
    temp = os.path.join(os.path.expanduser('~'), '.vacationtestrc')
    rc.rc_file = Mock(return_value=temp)  # Don't affect our actual file
    assert os.path.isfile(temp) is False
    rc.touch_rc()  # Should create file
    assert os.path.isfile(temp) is True
    os.unlink(temp)  # Cleanup
    assert os.path.isfile(temp) is False

