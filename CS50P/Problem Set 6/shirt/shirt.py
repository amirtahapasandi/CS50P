from PIL import Image, ImageOps
from sys import argv, exit
from os.path import splitext

def main():
    arg_len = len(argv)
    if arg_len < 3:
        exit("Too few command-line arguments")
    elif arg_len > 3:
        exit("Too many command-line arguments")
    else:
        suffix = (".jpg",".jpeg",".png")
        user_input = splitext(argv[1])
        user_output = splitext(argv[2])
        if user_output[1].lower() not in suffix:
            exit("Invalid output")
        elif user_input[1].lower() != user_output[1].lower():
            exit("Input and output have different extensions")
        else:
            editor(input=argv[1],output=argv[2])

def editor(input,output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(im = shirt, mask = shirt)
            input_cropped.save(output)
    except FileNotFoundError:
        exit("Input does not exist")

if __name__ == "__main__":
    main()