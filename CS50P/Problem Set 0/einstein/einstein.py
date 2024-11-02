def main():
    mass = int(input("M: "))
    print(f"E: {formula(mass)}")

def formula(mass):
    lightVelocity = 3*(10**8)
    return mass * (lightVelocity**2)

main()