from random import choice
numbers = list(range(1,100))
random_number = choice(numbers)

while True:
    level = (input("Level: ")).isdigit()
    if level:
        while True:
            try:
                guess_user_number = int(input("Guess: "))
            except (ValueError):
                continue
            if guess_user_number > random_number:
                print("Too large!")
                continue
            elif guess_user_number < random_number:
                print("Too small!")
                continue
            else:
                print("Just right!")
                break

        break
    else:
        continue