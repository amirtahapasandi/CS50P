def main():
    print(shorten(word=""))

def shorten(word):
    user_sentence = input("Your sentence: ")
    for letter in ["a","A","e","E","i","I","o","O","u","U"]:
        if letter in user_sentence:
            user_sentence = user_sentence.replace(letter,"")
    return user_sentence

if __name__ == "__main__":
    main()