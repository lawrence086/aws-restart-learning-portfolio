PRAGMA foreign_keys = ON;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    amount_cents INTEGER NOT NULL CHECK (amount_cents >= 0),
    status TEXT NOT NULL CHECK (status IN ('paid', 'pending'))
);

INSERT INTO customers (id, name) VALUES
    (1, 'Lerato'), (2, 'Thabo'), (3, 'Amina');

INSERT INTO orders (id, customer_id, amount_cents, status) VALUES
    (101, 1, 15000, 'paid'),
    (102, 1, 7500, 'pending'),
    (103, 2, 25000, 'paid');
