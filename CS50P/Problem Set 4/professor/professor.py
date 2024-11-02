import random

def main():
    level = get_level()
    score = main_game(level=level)
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            getting_level = int(input("Level: "))
            if getting_level in {1, 2, 3}:
                break
        except Exception:
            pass
    return getting_level

def generate_integer(level):
    if level == 1:
        x,y = random.randint(0,9) , random.randint(0,9)
    elif level == 2:
        x,y = random.randint(10,99) , random.randint(10,99)
    else:
        x,y = random.randint(100,999) , random.randint(100,999)
    return x,y

def generate_round(x:int,y:int):
    tries = 1
    while tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            result = x + y
            if answer == result:
                return True
            tries += 1
            print("EEE")
        except Exception:
            tries += 1
            print("EEE")
    print(f"{x} + {y} = {result}")
    return False

def main_game(level):
    rounds = 1
    score = 0
    while rounds <= 10:
        x,y = generate_integer(level)
        response = generate_round(x,y)
        if response == True:
            score += 1
        rounds += 1
    return score

if __name__ == "__main__":
    main()