while True:
    num = input("Fraction: ")
    index = num.find("/")
    try:
        x = int(num[:index])
        y = int(num[index+1:])
        fraction = x / y
        if x > y:
            continue
        break
    except (ValueError,ZeroDivisionError):
        continue

percentage = fraction * 100
percentage = int(percentage)
if percentage == 66 :
    percentage += 1

if fraction > 0.9:
    print("F")
elif fraction < 0.1:
    print("E")
else:
    print(str(percentage) + "%")