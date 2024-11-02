import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*></iframe>", s):
        url = re.search(r"(http(s)*://(www.)*youtube.com/embed/)([a-z_A-z_0-9]+)", s)
        if url:
            split_url = url.groups()
            return f"https://youtu.be/{split_url[3]}"


if __name__ == "__main__":
    main()