from sys import argv,exit
from pyfiglet import Figlet
from random import choice

figlet = Figlet()

if len(argv) == 1:
    font = True
elif len(argv) == 3 and (argv[1] == "--font" or argv[1] == "-f"):
    font = False
else:
    print("Invalid usage")
    exit(1)

# You can get fonts with this code:
figlet.getFonts()

if font == False:
    try:
        figlet.setFont(font=argv[2])
    except:
        print("Invalid usage")
        exit(1)
else:
    random_font = choice(figlet.getFonts())

message = input("Input:")
print("Output:")
print(figlet.renderText(message))