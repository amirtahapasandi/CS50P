from csv import DictReader,DictWriter
from sys import argv,exit

if len(argv) < 3:
    exit("Too few command-line arguments")
if len(argv) > 3:
    exit("Too many command-line arguments")
the_out_put = []
try:
    # Read csvfile
    with open(argv[1]) as csvfile:
        lines_reader = DictReader(csvfile)
        for line in lines_reader:
            splited_name = line["name"].split(",")
            the_out_put.append({"first":splited_name[1].lstrip(), "last":splited_name[0], "house": line["house"]})
except FileNotFoundError:
    exit(f"Could not read {argv[1]}")

# Write new csvfile
with open(argv[2],"w") as csvfile:
    lines_writer = DictWriter(csvfile, fieldnames=["first","last","house"])
    lines_writer.writerow({"first": "first", "last": "last", "house": "house"})
    for row in the_out_put:
        lines_writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})