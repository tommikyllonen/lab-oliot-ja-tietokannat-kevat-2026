--Query for T4 database
SELECT r.cashier, r.created_at AS receipt_date, p.name AS product_name, p.price_per_kilo, pr.amount
    FROM receipt r
    JOIN product_receipt pr ON r.id = pr.receipt_id
    JOIN product p ON pr.product_id = p.id
    WHERE r.cashier = 'Vincent'
ORDER BY r.created_at DESC;