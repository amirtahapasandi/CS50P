from numb3rs import validate

def main():
     test_first_byte()
     test_five_byte()


def test_first_byte():
      assert validate("1.2.3.4")==True
      assert validate("1.2.3")==False
      assert validate("1.2")==False
      assert validate("1")==False

def test_five_byte():
      assert validate("255.255.255.255")==True
      assert validate("512.1.1.1")==False
      assert validate("1.512.1.1")==False
      assert validate("1.1.512.1")==False
      assert validate("1.1.1.512")==False