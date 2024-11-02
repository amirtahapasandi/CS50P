def main():
    f = input("Fraction: ")
    f_c = convert(f) # f_c --> fraction_converted
    o_p = gauge(f_c) # o_p --> out_put
    print(o_p)

def convert(fraction):
    x,y = fraction.split("/")
    x = int(x)
    y = int(y)
    divided = x / y
    try:
        if divided <= 1:
            p = int(divided * 100)
            return p
        else:
            fraction = input("Fraction: ")
            pass
    except (ValueError,ZeroDivisionError):
        raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()