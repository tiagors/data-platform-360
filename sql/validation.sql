-- ============================================
-- Data Validation
-- ============================================


# Validar quantidade de registros
SELECT COUNT(*) AS total_clientes
FROM customers;


# Validar valores nulos
SELECT *
FROM customers
WHERE customer_id IS NULL
   OR first_name IS NULL
   OR last_name IS NULL
   OR email IS NULL;


# Validar duplicidades
SELECT
    customer_id,
    COUNT(*) AS quantidade
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;


# Quantidade de clientes distintos
SELECT
    COUNT(distinct(customer_id))
FROM customers


# Data mínima
SELECT
    min(created_at)
FROM customers;


# Data máxima
SELECT
    max(created_at)
FROM customers;

 



