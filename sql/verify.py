"""Check the shop queries and practise changes without keeping them."""

import sqlite3
from pathlib import Path


def check(actual, expected):
    if actual != expected:
        raise AssertionError(f"Expected {expected!r}, received {actual!r}")


def main():
    folder = Path(__file__).parent
    with sqlite3.connect(":memory:") as database:
        database.executescript((folder / "setup.sql").read_text())
        queries = (folder / "queries.sql").read_text().split(";")
        results = [database.execute(query).fetchall() for query in queries if query.strip()]
        check(results, [
            [(103, 25000), (101, 15000)],
            [(101, "Lerato", "paid"), (102, "Lerato", "pending"), (103, "Thabo", "paid")],
            [("Lerato", 2, 22500), ("Thabo", 1, 25000), ("Amina", 0, 0)],
            [("Amina",)],
        ])
        print("Checked four SELECT queries.")

        database.execute("BEGIN")
        database.execute("INSERT INTO orders VALUES (?, ?, ?, ?)", (104, 3, 5000, "pending"))
        database.execute("UPDATE orders SET status = ? WHERE id = ?", ("paid", 102))
        database.execute("DELETE FROM orders WHERE id = ?", (101,))
        check(database.execute("SELECT id, status FROM orders ORDER BY id").fetchall(),
              [(102, "paid"), (103, "paid"), (104, "pending")])
        database.rollback()
        check(database.execute("SELECT id, status FROM orders ORDER BY id").fetchall(),
              [(101, "paid"), (102, "pending"), (103, "paid")])
        print("Checked INSERT, UPDATE, DELETE and ROLLBACK.")

        try:
            database.execute("INSERT INTO orders VALUES (105, 99, 1000, 'paid')")
        except sqlite3.IntegrityError:
            database.rollback()
        else:
            raise AssertionError("An order with an unknown customer should be rejected.")
        print("Checked the customer foreign key.")
    print("All SQL checks passed.")


if __name__ == "__main__":
    main()
