# Kod źródłowy z użyciem wyrażeń listowych (list comprehensions)
import csv


# Przykładowa funkcja do analizy danych
def analyze_data_with_comprehensions(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        sales_values = [
            float(row["value"])
            for row in reader
            if row["variable"] == "Sales, government funding, grants and subsidies"
            and row["unit"] == "DOLLARS(millions)"
            and row["value"] != "C"
        ]
        average_sales = sum(sales_values) / len(sales_values) if sales_values else 0
        print(f"Average Sales: {average_sales}")

def main():
    # Wywołanie funkcji
    analyze_data_with_comprehensions("data.csv")


if __name__ == "__main__":
    main()