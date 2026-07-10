import csv
from operator import contains


def main():
    path: str = "data/dump_2026_yearly/csv/cities.csv"
    search_string: str = "Flagstaff"
    # path: str = input("Enter a path to a csv file: ")
    # search_string: str = input("Enter a search term: ")
    try:
        with open(path, "r") as file:
            dialect = csv.Sniffer().sniff(file.read(2048))
            file.seek(0)
            reader = csv.reader(file, dialect=dialect)
            header_row = next(reader)
            cities: list = []
            for row in reader:
                city: dict = {}
                for i in range(len(header_row)):
                    city[header_row[i]] = row[i]
                cities.append(city)
            for city in cities:
                if search_string in city.values():
                    for key, value in city.items():
                        print(f"{key}: {value}")

    except FileNotFoundError:
        print(f"Could not find file: {path}")


if __name__ == "__main__":
    main()
