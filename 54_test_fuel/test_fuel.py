from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/3") == 33
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_convert_exception():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("1//2")
    with pytest.raises(ValueError):
        convert("1%2")
    with pytest.raises(ValueError):
        convert("a/2")
    with pytest.raises(ValueError):
        convert("1/b")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
