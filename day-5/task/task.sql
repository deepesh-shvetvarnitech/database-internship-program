CREATE TABLE orders(
    order_id	INT	PRIMARY KEY,
    customer_name	VARCHAR(100)	NOT NULL,
    restaurant_name	VARCHAR(100)	NOT NULL,
    city	VARCHAR(50)	NOT NULL,
    order_amount	DECIMAL(10,2)	NOT NULL,
    order_status	VARCHAR(20)	NOT NULL
);
-- INSERT INTO orders (order_id,customer_name,restaurant_name,city,order_amount,order_status)
-- VALUES
-- (1	,'Rahul',	'Pizza Hub',	'Indore',	550.00,	'Delivered'),
-- (2,	'Priya',	'Burger Point',	'Bhopal',	320.00,	'Delivered'),
-- (3,	'Aman',	'Pizza Hub','Indore',	720.00,	'Delivered'),
-- (4,	'Neha'	,'Food Corner'	,'Ujjain'	,450.00	,'Cancelled'),
-- (5,	'Rohan',	'Burger Point',	'Indore'	,380.00	,'Delivered'),
-- (6,	'Anjali',	'Pizza Hub',	'Indore',	640.00,	'Pending'),
-- (7,	'Karan',	'Food Corner',	'Bhopal',	510.00,	'Delivered'),
-- (8,	'Sneha',	'Burger Point',	'Indore',	290.00,	'Delivered'),
-- (9,	'Vikas',	'Pizza Hub',	'Ujjain',	900.00	,'Delivered'),
-- (10,	'Pooja',	'Food Corner',	'Indore',	650.00,	'Delivered');
-- SELECT * FROM orders;
-- SELECT customer_name ,restaurant_name , order_amount FROM  orders;
-- SELECT * FROM orders WHERE order_status = 'Delivered';
-- SELECT * FROM orders WHERE restaurant_name IN ('Pizza Hub','Burger Point');
-- SELECT * FROM orders WHERE customer_name LIKE 'P%';
-- SELECT * FROM orders WHERE order_amount BETWEEN 300 AND 700;
-- SELECT * FROM orders ORDER BY order_amount ASC;
-- SELECT * FROM orders ORDER BY order_amount DESC LIMIT 3;
-- SELECT DISTINCT city FROM orders;
SELECT COUNT(*) AS total_order FROM orders;
SELECT SUM(order_amount) AS delivered_revenue FROM orders WHERE order_status = 'Delivered';
SELECT AVG(order_amount) AS average_order_amount FROM orders;
SELECT MAX(order_amount) AS highest_order_amount FROM orders;
SELECT MIN(order_amount) AS lowestt_order_amount FROM orders;
SELECT restaurant_name, SUM (order_amount) AS revenue FROM orders GROUP BY restaurant_name;
SELECT city, AVG(order_amount) AS average_order FROM orders GROUP BY city;
SELECT restaurant_name, COUNT(*) AS total_order FROM orders GROUP BY restaurant_name HAVING SUM (order_amount) >1500; 
SELECT * FROM orders ORDER BY restaurant_name,customer_name;
SELECT restaurant_name, COUNT(*) AS Delivered_order FROM orders WHERE order_status = 'Delivered' GROUP BY 
restaurant_name;
SELECT city, COUNT(*) AS total_order FROM orders GROUP BY city HAVING COUNT(*) > 2;
SELECT restaurant_name, AVG(order_amount) average_order_value FROM orders GROUP BY restaurant_name ORDER BY
average_order_value DESC LIMIT 1;
SELECT DISTINCT restaurant_name FROM orders WHERE restaurant_name LIKE 'P%' ORDER BY restaurant_name ASC;











