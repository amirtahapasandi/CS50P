def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(x):
    counter = 0
    if x[0:2].isalpha():
        counter += 1
    else:
        counter -= 1

    if 2 <= len(x) <= 6:
        counter += 1
    else:
        counter -= 1

    for i in range(len(x)):
        if x[i].isdigit():
            if x[i] != "0":
                if x[i:].isdigit():
                    counter += 1
                    break
                else:
                    counter -= 1
                    break
            else:
                counter -= 1
                break
    if x.isalpha():
        counter += 1

    p_m = ("!","?","-",","," ") # p_m --> Punk Mark
    for i in p_m:
        if i in x:
            counter -= 1
    else:
        counter += 1
    if counter == 4:
        return True
    else:
        return False

if __name__ == "__main__":
    main()