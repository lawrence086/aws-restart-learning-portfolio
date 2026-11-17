# SQL practice

During the programme I worked with MySQL, including database clients on EC2 and managed databases in AWS. This folder is a small local revision exercise using SQLite, which comes with Python.

- [setup.sql](setup.sql) creates fictional customers and orders in a fresh database.
- [queries.sql](queries.sql) practises filters, joins, totals and finding customers without orders.
- [verify.py](verify.py) runs those queries in memory, checks their results and demonstrates a transaction rollback.

```sh
python3 sql/verify.py
```

The output should finish with `All SQL checks passed.` I store amounts in whole cents to keep the arithmetic exact.

I used a left join to find customers who had never placed an order. Before running an `UPDATE` or `DELETE`, I use a `SELECT` to check which rows match.
