from bank import value

def test_greeting_starts_with_hello():
    assert value("hello") == 0
 #   assert value(" hello") == 0
    assert value("Hello") == 0
    assert value("HeLlO") == 0
    assert value("hello Mr. X") == 0


def test_greeting_starts_with_h():
    assert value("hi") == 20
    assert value("Hi") == 20
#    assert value(" Hi") == 20
#    assert value(" hi") == 20
    assert value("hi Mr. X") == 20


def test_greeting_starts_with_something_else():
    assert value("Dobrij Den") == 100
    assert value("Priwet") == 100
    assert value("12kjfw") == 100
    assert value("12.-*?") == 100
    assert value("?*'SASFD") == 100