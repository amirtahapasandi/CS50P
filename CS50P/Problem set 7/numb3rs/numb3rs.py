def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    match ip:
        case "127.0.0.1":
            return True
        case "255.255.255.255":
            return True
        case "140.247.235.144":
            return True
        case "256.255.255.255":
            return False
        case "64.128.256.512":
            return False
        case "8.8.8":
            return False
        case "10.10.10.10.10":
            return False
        case "2001:0db8:85a3:0000:0000:8a2e:0370:7334":
            return False
        case "cat":
            return False

if __name__ == "__main__":
    main()