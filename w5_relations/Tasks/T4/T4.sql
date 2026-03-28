CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    price_per_kilo NUMERIC NOT NULL
);
INSERT INTO product (name, price_per_kilo) VALUES
('Chunkies', 8),
('Rifrafs', 7),
('Rumbles', 9.5),
('Yumyums', 6),
('Salmarish', 10);




CREATE TABLE IF NOT EXISTS receipt (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cashier TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO receipt (id, cashier, created_at) VALUES
(1, 'Alice', 1672531200),
(2, 'Alice', 1672617600),
(3, 'Alice', 1672704000),
(4, 'Alice', 1672790400),
(5, 'Alice', 1672876800),
(6, 'Alice', 1672963200),
(7, 'Alice', 1673049600),
(8, 'Hannah', 1673136000),
(9, 'Hannah', 1673222400),
(10, 'Hannah', 1673308800),
(11, 'Hannah', 1673395200),
(12, 'Hannah', 1673481600),
(13, 'Hannah', 1673568000),
(14, 'Hannah', 1673654400),
(15, 'Hannah', 1673740800),
(16, 'Hannah', 1673827200),
(17, 'Vincent', 1673913600),
(18, 'Vincent', 1674000000),
(19, 'Vincent', 1674086400),
(20, 'Vincent', 1674172800),
(21, 'Vincent', 1674259200),
(22, 'Vincent', 1674345600),
(23, 'Vincent', 1674432000),
(24, 'Vincent', 1674518400),
(25, 'Vincent', 1674604800),
(26, 'Vincent', 1674691200);


CREATE TABLE IF NOT EXISTS product_receipt (
    amount NUMERIC NOT NULL,
    product_id INTEGER NOT NULL,
    receipt_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (receipt_id) REFERENCES receipt(id)
);

INSERT INTO product_receipt (amount, product_id, receipt_id) VALUES
(0.8, 2, 1),
(1.2, 4, 2),
(1.4, 1, 3),
(0.6, 3, 4),
(1.1, 5, 5),
(1.5, 2, 6),
(0.9, 4, 7),
(1.6, 1, 8),
(1, 3, 9),
(0.7, 5, 10),
(1.3, 2, 11),
(1.1, 4, 12),
(0.5, 1, 13),
(0.7, 3, 14),
(1.4, 5, 15),
(1.2, 2, 16),
(0.8, 4, 17),
(1.5, 1, 18),
(0.9, 3, 19),
(1, 5, 20),
(0.6, 2, 21),
(1, 4, 22),
(1.3, 1, 23),
(1.6, 3, 24),
(0.5, 5, 25),
(1.1, 2, 26);