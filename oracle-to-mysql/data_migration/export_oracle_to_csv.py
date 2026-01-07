import csv

rows = [
    (1, "Ali Ahmadi", "ali@test.com", "2024-01-01"),
    (2, "Sara Karimi", "sara@test.com", "2024-01-02"),
]

with open("customers.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["customer_id", "full_name", "email", "created_at"])
    w.writerows(rows)
