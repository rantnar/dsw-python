def main():
    while True:
        try:
            date = input("Podaj datę (format: RRRR-MM-DD): ")
            year, month, day = map(int, date.split("-"))
            if year < 1900 or year > 2024:
                raise ValueError("Nieprawidłowy rok")
            if month < 1 or month > 12:
                raise ValueError("Nieprawidłowy miesiąc")
            if day < 1 or day > 31:
                raise ValueError("Nieprawidłowy dzień")
            print(f"Data: {year}-{month:02d}-{day:02d}")
            break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
