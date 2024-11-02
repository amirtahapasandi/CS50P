from sys import argv,exit

def check_empty_and_comment_lines(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

if len(argv) == 1:
    exit("Too few command-line arguments")
if len(argv) > 2:
    exit("Too many command-line arguments")
if ".py" not in argv[1]:
    exit("Not a Python file")

count = 0
try:
    with open(argv[1] ,"r") as file:
        for line in file:
            if check_empty_and_comment_lines(line) == False:
                count += 1
        print(count)
except FileNotFoundError:
    exit("File does not exist")