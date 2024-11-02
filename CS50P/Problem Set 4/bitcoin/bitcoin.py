from requests import get,RequestException
from sys import argv,exit

try:
    price = get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    final_bitcoin_price = float((price["bpi"]["USD"]["rate"]).replace(",","")) * float(argv[1])
    print(f"${final_bitcoin_price:,}")
except IndexError:
    print("Missing command-line argument")
    exit(1)
except ValueError:
    print("Command-line argument is not a number")
    exit(1)
except RequestException:
    print("Server isn't accessible!")
    exit(1)