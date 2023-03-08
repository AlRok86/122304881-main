from numb3rs import validate


def test_IPV4_numbers():
    assert validate("1.2.3.4")
    assert validate("11.21.31.41")
    assert validate("255.255.255.255")
    assert validate("0.0.0.0")
    assert validate("0.10.100.255")
    assert validate("255.0.1.0")
    assert not validate("255.0.257.0")
    assert not validate("256.0.0.0")
    assert not validate("-1.0.0.0")
    assert not validate("0.-1.0.0")
    assert not validate("A.0.0.0")
    assert not validate("0.A.0.0")
    assert not validate("0.0.A.0")
    assert not validate("A.0.0.A")


def test_IPV4_other_separator():
    assert not validate("1,2,3,4")
    assert not validate("1:2:3:4")


def test_IPV4_different_size():
    assert not validate("1.2.3")
    assert not validate("1.2")
