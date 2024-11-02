from plates import is_valid

def test_one():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5") == False

def test_second():
    assert is_valid("HHCS50") == True
    assert is_valid("CG") == True
    assert is_valid("HELLCS50") == False

def test_third():
    assert is_valid("AAA87A") == False
    assert is_valid("AAA098") == False
    assert is_valid("AAA767") == True

def test_fourth():
    assert is_valid("CS60!") == False