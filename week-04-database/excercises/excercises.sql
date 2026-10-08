SELECT SUM(price * stock_quantity) FROM products WHERE stock_quantity > 0 AND category = 'Electronics'

SELECT COUNT(name) FROM products WHERE price is NULL

SELECT MIN(price), MAX(price), AVG(price) FROM products

SELECT MAX(release_date) FROM products

SELECT COUNT(price) FROM products

SELECT AVG(price) FROM products WHERE price > 50.00

SELECT MIN(name) FROM products




SELECT product_category, SUM(purchase_amount) FROM sales_transactions GROUP BY product_category

SELECT payment_method, COUNT(*) FROM sales_transactions GROUP BY payment_method

SELECT store_branch,  AVG(purchase_amount) FROM sales_transactions GROUP BY store_branch

SELECT customer_id, MAX(purchase_amount) FROM sales_transactions GROUP BY customer_id

SELECT store_branch, payment_method, SUM(purchase_amount) FROM sales_transactions GROUP BY store_branch, payment_method




SELECT agent_name , COUNT(*) FROM support_tickets GROUP BY agent_name HAVING COUNT(*) > 2

SELECT category, AVG(resolution_time_hours) FROM support_tickets GROUP BY category HAVING AVG(resolution_time_hours) > 10

SELECT agent_name , COUNT(*) FROM support_tickets WHERE priority = 'critical' GROUP BY agent_name HAVING COUNT(*) >= 1

SELECT agent_name, AVG(resolution_time_hours) FROM support_tickets WHERE status ='closed' GROUP BY agent_name HAVING AVG(resolution_time_hours) < 6

SELECT agent_name, MAX(resolution_time_hours) FROM support_tickets WHERE category = 'Billing' GROUP BY agent_name HAVING MAX(resolution_time_hours) > 5



Practie:

SELECT COUNT(*) FROM customers

SELECT COUNT(*) FROM orders

SELECT MAX(unit_price) FROM order_items

SELECT SUM(quantity * unit_price) FROM order_items

SELECT AVG(quantity *unit_price) FROM order_items

SELECT order_id, SUM(quantity * unit_price) FROM order_items GROUP BY order_id ORDER BY SUM(quantity * unit_price) DESC;



