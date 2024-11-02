from re import search


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = search(r"^" + regex + " to " + regex + "$", s)
    if match:
        from_time = new_time(match.group(1), match.group(2), match.group(3))
        time = new_time(match.group(4), match.group(5), match.group(6))
        return f"{from_time} to {time}"
    else:
        raise ValueError


def new_time(hour, min, y):
    if hour == "12":
        if y == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if y == "AM":
            hour = f"{int(hour):02}"
        else:
            hour = f"{int(hour)+12}"
    if min == None:
        minute = "00"
    else:
        minute = f"{int(min):02}"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()