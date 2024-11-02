grocery = {}

while True:
    try:
        item = input()
    except EOFError:
        print()
        break
    if item.upper() in grocery:
        grocery[item.upper()] += 1
    else:
        grocery[item.upper()] = 1

for item in sorted(grocery.keys()):
    print(grocery[item], item )