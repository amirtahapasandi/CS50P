from datetime import date
from operator import sub
from sys import exit
import inflect


p = inflect.engine() # Create an instance of the inflect engine


def main():
    try:
        user_date = input("Date of Birth: ")
        subtracted = sub(date.today(), date.fromisoformat(user_date)) # Calculate the difference between today's date and the user's input date
        print(convert(subtracted.days)) # Convert the difference in days to words and print it
    except ValueError:
        exit("Invalid date")

def convert(days):
    minutes = days * 24 * 60 # Calculate the age in minutes from the age in days
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes" # Convert the age in minutes to words, capitalize the result, and append "minutes"



if __name__ == "__main__":
    main()