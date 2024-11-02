import validators

user_address = input("What's your email address? ").lower()

if validators.email(user_address):
    print("Valid")
else:
    print("Invalid")