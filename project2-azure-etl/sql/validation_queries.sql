SELECT COUNT(*) FROM customers;

SELECT TOP 10 * FROM customers;

SELECT city, COUNT(*) AS total_customers
FROM customers
GROUP BY city;

SELECT AVG(revenue) AS avg_revenue
FROM customers;