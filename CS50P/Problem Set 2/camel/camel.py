user_input = input("camel case:")
out_put = ""
for letter in user_input:
    if letter.islower():
        out_put += letter
    else:
        out_put += ("_" + letter.lower())
else:
    print(f"snake case:{out_put}")