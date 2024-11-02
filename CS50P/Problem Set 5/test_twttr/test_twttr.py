from twttr import shorten

def main():
    test_1()

def test_1():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TWITTER10") == "TWTTR10"
    assert shorten("?TWITTER?") == "?TWTTR?"

if __name__ == "__main__":
    main()