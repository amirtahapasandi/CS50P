from seasons import convert


def test_convert():
    assert convert(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"