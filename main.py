import csv
from operator import contains


def main():
    path: str = input("Enter a path to a csv file: ")
    search_string: str = input("Enter a search term: ")
    try:
        with open(path, "r") as file:
            dialect = csv.Sniffer().sniff(file.read(2048))
            file.seek(0)
            reader = csv.reader(file, dialect=dialect)
            header_row = next(reader)
            print(header_row)
            for row in reader:
                if search_string in row:
                    print(row)

    except FileNotFoundError:
        print(f"Could not find file: {path}")


if __name__ == "__main__":
    main()
