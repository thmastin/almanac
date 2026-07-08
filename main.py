import csv

path = "data/dump_2026_yearly/csv/teams.csv"


def main():
    try:
        with open(path, "r") as file:
            dialect = csv.Sniffer().sniff(file.read(2048))
            file.seek(0)
            reader = csv.reader(file, dialect=dialect)
            print(next(reader))
            for row in reader:
                print(row)

    except FileNotFoundError:
        print(f"Could not find file: {path}")


if __name__ == "__main__":
    main()
