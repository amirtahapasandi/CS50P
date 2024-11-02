ms = ["January","February","March","April","May","June","July","August","September","October","November","December"]
# y = year , d = day , m = month , ms = months
while True:
    user_date = input("Date: ")
    try:
        if "/" in user_date:
            m, d, y = user_date.split("/")
        elif "," in user_date:
            other, y = user_date.split(", ")
            m, d = other.split(" ")
            m = (ms.index(m)) + 1
        if int(m) > 12 or int(d) > 31:
            raise ValueError
    except (ValueError, NameError, KeyError, AttributeError):
        pass
    else:
        print(f"{int(y)}-{int(m):02}-{int(d):02}")
        break