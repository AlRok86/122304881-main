from twttr import shorten

def test_shorten_lowercase_words():
    assert shorten("apple") == "ppl"
    assert shorten("mango") == "mng"
    assert shorten("floor") == "flr"
    assert shorten("tiger") == "tgr"

def test_shorten_uppercase_words():
    assert shorten("APPLE") == "PPL"
    assert shorten("MANGO") == "MNG"
    assert shorten("FLOOR") == "FLR"
    assert shorten("TIGER") == "TGR"

def test_shorten_sentence():
    assert shorten("My name is Alex") == "My nm s lx"
    assert shorten("Lions are scary") == "Lns r scry"
    assert shorten("Space is large") == "Spc s lrg"

def test_shorten_punctuation():
    assert shorten(".,-;") == ".,-;"

def test_shorten_number():
    assert shorten("1234567890") == "1234567890"