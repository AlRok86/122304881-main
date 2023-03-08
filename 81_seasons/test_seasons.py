from seasons import get_birthday
from seasons import get_date_diff_in_minutes
from datetime import date
import pytest


def test_get_birthday():
    assert get_birthday("1986-12-8") == date(1986, 12, 8)
    assert get_birthday("1986-4-4") == date(1986, 4, 4)
    assert get_birthday("1986-12-31") == date(1986, 12, 31)
    with pytest.raises(ValueError):
        get_birthday("2000-11-31")
    with pytest.raises(ValueError):
        get_birthday("2003-2-29")
    with pytest.raises(ValueError):
        get_birthday("2000-13-1")


def test_date_diff_in_minutes():
    assert get_date_diff_in_minutes(date(2001,1,1),date(2000,1,1)) == 366 * 24 * 60
    assert get_date_diff_in_minutes(date(2002,1,1),date(2001,1,1)) == 365 * 24 * 60