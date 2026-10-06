DROP TABLE IF EXISTS customers;

DROP TABLE IF EXISTS products;

CREATE TABLE IF NOT EXISTS customers(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
country TEXT,
email TEXT
);

CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
price REAL,
stock INTEGER
);

INSERT INTO customers(name, country, email) VALUES ('Neha','UK', 'neha@gmail.com'), ('Aneen', 'England', 'aneenxo@yahoo.com'),
('Liam', 'Ireland', NULL),
('Sofia', NULL, 'sofia.martinez@gmail.com'),
('Mateo', 'Mexico', 'mateo.r@yahoo.com'),
('Aisha', 'UAE', 'aisha.k@hotmail.com'),
('Lucas', 'Brazil', NULL),
('Yuki', 'Japan', 'yuki.tanaka@yahoo.co.jp'),
('Hannah', NULL, NULL),
('Chloe', 'France', 'chloe.dubois@orange.fr'),
('Arjun', 'India', 'arjun.patel@gmail.com'),
('Elena', 'Italy', NULL),
('Noah', NULL, 'noah.w@outlook.com'),
('Mia', 'Australia', 'mia.jones@gmail.com'),
('Lars', 'Sweden', 'lars.lind@tele2.se'),
('Fatima', 'Morocco', NULL),
('David', 'United States', 'david.miller@gmail.com'),
('Min-jun', NULL, 'minjun.kim@naver.com'),
('Zoe', 'New Zealand', 'zoe.taylor@gmail.com'),
('Oliver', NULL, NULL);


SELECT * FROM customers;

INSERT INTO products(name, price, stock) VALUES
('Wireless Mouse', 29.99, 150),
('Mechanical Keyboard', 89.99, 45),
('Bluetooth Speaker', NULL, 80),
('HDMI Cable 2m', 12.50, NULL),
('27-inch Monitor', 249.99, 20),
('USB-C Flash Drive', 19.99, 300),
('Ergonomic Office Chair', 189.00, NULL),
('Desk Pad Mat', 15.00, 75),
('Noise Cancelling Headphones', 149.99, 35),
('Webcam 1080p', NULL, 60),
('External Hard Drive 1TB', 59.99, 110),
('Laptop Stand', 34.99, 90),
('Smart Fitness Watch', 120.00, NULL),
('Rechargeable AA Batteries', 18.50, 200),
('LED Desk Lamp', NULL, NULL),
('Portable Power Bank', 45.00, 130),
('Wireless Earbuds', 79.99, 65),
('Gaming Mouse Pad', 22.00, 140),
('USB Hub 4-Port', NULL, 85),
('Smartphone Case', 12.99, NULL);

SELECT * FROM products;

SELECT 'customers' AS table_name, COUNT(*) AS row_count FROM customers
UNION ALL
SELECT 'products' AS table_name, COUNT(*) AS row_count FROM products;

SELECT * FROM customers WHERE country = 'India';

SELECT * FROM products WHERE price > 100.00;

SELECT * FROM products WHERE price IS NOT NULL ORDER BY price ASC LIMIT 1;

SELECT * FROM products WHERE price IS NOT NULL ORDER BY price DESC LIMIT 5;

SELECT * FROM customers WHERE name LIKE 'An%';

SELECT * FROM products WHERE stock = 0 OR stock IS NULL;

UPDATE products SET stock = 3 where name = 'LED DESK LAMP';

SELECT * FROM products WHERE name = 'LED DESK LAMP';

DELETE FROM customers WHERE name = 'Hannah';

SELECT * FROM customers WHERE country IS NULL OR email IS NULL;