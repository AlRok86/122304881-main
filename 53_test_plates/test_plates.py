from plates import is_valid

def test_start2letter():
    assert is_valid("aa1") == True
    assert is_valid("Aa1") == True
    assert is_valid("aaaaaa") == True
    assert is_valid("1a") == False
    assert is_valid("a1") == False

def test_min2chara_max6char():
    assert is_valid("aa") == True
    assert is_valid("aaa") == True
    assert is_valid("aaaaaa") == True
    assert is_valid("a") == False
    assert is_valid("aaaaaaa") == False

def test_number_at_end():
    assert is_valid("aa123") == True
    assert is_valid("aa234") == True
    assert is_valid("aa456") == True
    assert is_valid("aa123a") == False
    assert is_valid("aa1a23") == False

def test_firstnumber_not0():
    assert is_valid("aa123") == True
    assert is_valid("aa1230") == True
    assert is_valid("aa1024") == True
    assert is_valid("aa0") == False
    assert is_valid("aa0123") == False

def test_no_punctuation():
    assert is_valid("aa123.") == False
    assert is_valid("aa,") == False
    assert is_valid("aa-") == False
    assert is_valid("aa?") == False
    assert is_valid("aa ") == False
    assert is_valid(" aa123") == False