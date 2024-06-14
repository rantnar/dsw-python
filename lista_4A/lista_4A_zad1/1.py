import datetime

def main():
    while True:
        try:
            date = input("Podaj datę urodzenia (format: RRRR-MM-DD): ")
            year, month, day = map(int, date.split("-"))
            if year < 1900 or year > datetime.datetime.now().year:
                raise ValueError("Nieprawidłowy rok")
            if month < 1 or month > 12:
                raise ValueError("Nieprawidłowy miesiąc")
            if day < 1 or day > 31:
                raise ValueError("Nieprawidłowy dzień")
            birth_date = datetime.date(year, month, day)
            age = (datetime.date.today() - birth_date).days
            print(f"Wiek: {age} dni")
            break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
