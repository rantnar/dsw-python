# Prosta Analiza Zbioru Danych Statystycznych

# Zadanie

1. Pobierz zbiór danych ze strony [Statistics New Zealand](https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2021-financial-year-provisional/Download-data/annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv).
2. Zapoznaj się ze strukturą i zawartością zbioru danych.
3. Przeanalizuj dwa dostarczone kody źródłowe wykonujące analizę danych - jedną z użyciem pętli, drugą z użyciem list comprehensions.
4. Uruchom oba programy i porównaj wyniki.
5. Zmodyfikuj programy wyciągając obliczanie średniej do funkcji `calculate_average`
6. Dodaj funkcję `calculate_median` według przykładu i jej użyj w programach
7. Wymyśl dodatkową analizę oraz rozbuduj programy - jaką pozostawiaj Twojej inwencji
8. Przygotuj raport zawierający twoje spostrzeżenia, uzyskane wyniki oraz przygotowane kody źródłowe.

# Kod programu

```python
import csv

def calculate_average(values):
    total_sales = sum(values)
    count = len(values)
    return total_sales / count if count else 0

def calculate_median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n % 2 == 1:
        return sorted_values[n // 2]
    else:
        return (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2

def lowest_sum(yearly_sums):
    min_year = min(yearly_sums, key=yearly_sums.get)
    return min_year, yearly_sums[min_year]

def analyze_data(filename):
    with open(filename, "r", encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        values = []
        yearly_sums = {}
        for row in reader:
            if (
                row["variable"] == "Sales, government funding, grants and subsidies"
                and row["unit"] == "DOLLARS(millions)"
                and row["value"] != "C"
            ):
                year = row["year"]
                value = float(row["value"])
                values.append(value)
                if year in yearly_sums:
                    yearly_sums[year] += value
                else:
                    yearly_sums[year] = value
        average_sales = calculate_average(values)
        median_sales = calculate_median(values)
        min_year = lowest_sum(yearly_sums)
        print(f"Average Sales: {average_sales}")
        print(f"Median Sales: {median_sales}")
        print(f"Year with lowest sum of sales: {min_year}")
        
def main():
    analyze_data("data.csv")

if __name__ == "__main__":
    main()
```

## Opis funkcji

1. calculate_average - Ta funkcja oblicza średnią wartość z listy liczb
```python
def calculate_average(values):
    total_sales = sum(values)
    count = len(values)
    return total_sales / count if count else 0
```
2. calculate_median - Ta funkcja liczy mediane (średnią wartość) z listy liczb
```python
def calculate_median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n % 2 == 1:
        return sorted_values[n // 2]
    else:
        return (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2
```
3. lowest_sum - Ta funkcja znajduje rok z najniższą sumą sprzedaży.
```python
def lowest_sum(yearly_sums):
    min_year = min(yearly_sums, key=yearly_sums.get)
    return min_year, yearly_sums[min_year]
```

## Opis działania kodu

Na podstawie stworzonej wcześniej funkcji 'analyze_data_with_loops' utworzyłem funkcje analyze_data:
```python
def analyze_data(filename):
    with open(filename, "r", encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        values = []
        yearly_sums = {}
        for row in reader:
            if (
                row["variable"] == "Sales, government funding, grants and subsidies"
                and row["unit"] == "DOLLARS(millions)"
                and row["value"] != "C"
            ):
                year = row["year"]
                value = float(row["value"])
                values.append(value)
                if year in yearly_sums:
                    yearly_sums[year] += value
                else:
                    yearly_sums[year] = value
        average_sales = calculate_average(values)
        median_sales = calculate_median(values)
        min_year = lowest_sum(yearly_sums)
        print(f"Average Sales: {average_sales}")
        print(f"Median Sales: {median_sales}")
        print(f"Year with lowest sum of sales: {min_year}")
```
Jest to główna funkcja analizująca dane sprzedaży z pliku CSV.

Otwiera ona plik CSV, inicjalizuje listę values i słownik early_sums

- values przechowuje wszystkie wartości sprzedaży spełniające określone warunki

- yearly_sums przechowuje sumy sprzedaży dla każdego roku.
  
Pętla for sprawdza każy wiersz pliku CSV. Warunkami są:
- wiersz "variable" musi się równać "Sales, government funding, grants and subsidies"
- wiersz "unit" równa się "DOLLARS(millions)
- wiersz "value" nie wynosi "C"
  
Gdy te warunki są spełnione:
- Pobieram rok i wartość z wiersza oraz dodajemy ją do listy values
- Dodajemy rok do słownika yearly_sums. Jeżeli rok już istnieje dodajemy do niego wartość. Jeżeli rok nie istnieje dodawany jest nowy rok z początkową sumą.

Po przejściu przez wszystkie wiersze wywoływane są funkcję calculate_average, calculate_median, lowest_sum oraz wywoływane są na ekran wyniki tych funkcji.

Dla kodu powyżej dla danych z pliku CSV wynikami są:

```
Average Sales: 9836.639388979815
Median Sales: 1797.0
Year with lowest sum of sales: ('2011', 1339267.0)
```
