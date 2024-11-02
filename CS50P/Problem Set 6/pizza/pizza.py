from csv import reader
from sys import argv,exit
from tabulate import tabulate

if len(argv) == 1:
    exit("Too few command-line arguments")
if len(argv) > 2:
    exit("Too many command-line arguments")
if ".csv" not in argv[1]:
    exit("Not a CSV file")

table = []
try:
    with open(argv[1] ,"r") as csv_file:
        csv_reader = reader(csv_file)
        for row in csv_reader:
            table.append(row)
        print(tabulate(table[1:], headers = table[0], tablefmt = "grid"))
except FileNotFoundError:
    exit("File does not exist")