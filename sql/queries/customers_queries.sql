-- Todos os clientes
SELECT * FROM customers;

-- Total de clientes
SELECT COUNT(*) AS total_customers
FROM customers;

-- Clientes em ordem alfabética
SELECT *
FROM customers
ORDER BY last_name;

-- Buscar por e-mail
SELECT *
FROM customers
WHERE email = 'ana.silva@email.com';