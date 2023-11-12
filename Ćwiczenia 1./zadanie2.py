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