userInput = input("Your expression: ")
x, y, z = userInput.split(" ")

x = float(x)
z = float(z)

if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x*z)
elif y == "/":
    print(x/z)