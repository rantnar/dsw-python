import urllib.request
from urllib.error import URLError, HTTPError

def get_page_content():
    while True:
        try:
            url = input("Podaj adres URL: ")
            with urllib.request.urlopen(url) as response:
                return response.read().decode("utf-8")
        except (URLError, HTTPError):
            print("Nie można otworzyć strony. Spróbuj ponownie.")

def main():
    print(get_page_content())

if __name__ == "__main__":
    main()
