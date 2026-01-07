import csv

def load():
    with open("customers.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            print(f"INSERT customer {r['customer_id']}")

load()
