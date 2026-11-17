-- Paid orders above R100, largest first.
SELECT id, amount_cents
FROM orders
WHERE status = 'paid' AND amount_cents > 10000
ORDER BY amount_cents DESC;

-- Show who placed each order.
SELECT orders.id, customers.name, orders.status
FROM orders
JOIN customers ON customers.id = orders.customer_id
ORDER BY orders.id;

-- Include customers who have not placed any orders.
SELECT customers.name, COUNT(orders.id), COALESCE(SUM(orders.amount_cents), 0)
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.id
GROUP BY customers.id, customers.name
ORDER BY customers.id;

-- Find customers with no orders.
SELECT customers.name
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.id
WHERE orders.id IS NULL
ORDER BY customers.id;
