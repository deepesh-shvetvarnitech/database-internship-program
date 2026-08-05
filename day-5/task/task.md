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
# ![alt text](<Screenshot 2026-08-05 191404.png>)


-- SELECT customer_name ,restaurant_name , order_amount FROM  orders;
# ![alt text](<Screenshot 2026-08-05 191917.png>)
-- SELECT * FROM orders WHERE order_status = 'Delivered';
# ![alt text](<Screenshot 2026-08-05 192033.png>)
-- SELECT * FROM orders WHERE restaurant_name IN ('Pizza Hub','Burger Point');
# ![alt text](<Screenshot 2026-08-05 192215.png>)
-- SELECT * FROM orders WHERE customer_name LIKE 'P%';
# ![alt text](<Screenshot 2026-08-05 192345.png>)
-- SELECT * FROM orders WHERE order_amount BETWEEN 300 AND 700;
# ![alt text](<Screenshot 2026-08-05 192538.png>)
-- SELECT * FROM orders ORDER BY order_amount ASC;
# ![alt text](<Screenshot 2026-08-05 192833.png>)
-- SELECT * FROM orders ORDER BY order_amount DESC LIMIT 3;
# ![alt text](<Screenshot 2026-08-05 192845.png>)
-- SELECT DISTINCT city FROM orders;
# ![alt text](<Screenshot 2026-08-05 192950.png>)
SELECT COUNT(*) AS total_order FROM orders;
# ![alt text](<Screenshot 2026-08-05 193309.png>)
SELECT SUM(order_amount) AS delivered_revenue FROM orders WHERE order_status = 'Delivered';
# ![alt text](<Screenshot 2026-08-05 193705.png>)
SELECT AVG(order_amount) AS average_order_amount FROM orders;
# ![alt text](<Screenshot 2026-08-05 193840.png>)
SELECT MAX(order_amount) AS highest_order_amount FROM orders;
# ![alt text](<Screenshot 2026-08-05 194026.png>)
SELECT MIN(order_amount) AS lowestt_order_amount FROM orders;
# ![alt text](<Screenshot 2026-08-05 194118.png>)
SELECT restaurant_name, SUM (order_amount) AS revenue FROM orders GROUP BY restaurant_name;
# ![alt text](<Screenshot 2026-08-05 194837.png>)
SELECT city, AVG(order_amount) AS average_order FROM orders GROUP BY city;
# ![alt text](<Screenshot 2026-08-05 194849.png>)
SELECT restaurant_name, COUNT(*) AS total_order FROM orders GROUP BY restaurant_name HAVING SUM (order_amount) >1500; 
# ![alt text](<Screenshot 2026-08-05 195249.png>)
SELECT * FROM orders ORDER BY restaurant_name,customer_name;
# ![alt text](<Screenshot 2026-08-05 195424.png>)
SELECT restaurant_name, COUNT(*) AS Delivered_order FROM orders WHERE order_status = 'Delivered' GROUP BY 
restaurant_name;
# ![alt text](<Screenshot 2026-08-05 195726.png>)
SELECT city, COUNT(*) AS total_order FROM orders GROUP BY city HAVING COUNT(*) > 2;
# ![alt text](<Screenshot 2026-08-05 195935.png>)
SELECT restaurant_name, AVG(order_amount) average_order_value FROM orders GROUP BY restaurant_name ORDER BY
average_order_value DESC LIMIT 1;
# ![alt text](<Screenshot 2026-08-05 200248.png>)
SELECT DISTINCT restaurant_name FROM orders WHERE restaurant_name LIKE 'P%' ORDER BY restaurant_name ASC;
# ![alt text](<Screenshot 2026-08-05 200629.png>)

