def main():
    dollars = converter(input("How much was the meal? "),input("What percentage would you like to tip? "))
    print(f"Leave ${dollars:.2f}")

def converter(d,p):
    return (((float(p.replace("%","")))/100) * (float(d.replace("$",""))))

main()