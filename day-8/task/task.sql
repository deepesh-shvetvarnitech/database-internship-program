-- CREATE TABLE coustomers(
--   customer_id	INT	            PRIMARY KEY,
--   customer_name	VARCHAR(100)	NOT NULL,
--   email	        VARCHAR(100)	UNIQUE,
--   city	        VARCHAR(50)	    NOT NULL);
-- SELECT * FROM coustomers;

-- CREATE TABLE restaurants(
--     restaurant_id	INT	            PRIMARY KEY,
--     restaurant_name	VARCHAR(100)	NOT NULL,
--     city	        VARCHAR(50)	    NOT NULL
-- );
-- SELECT * FROM restaurants;


-- CREATE TABLE orders(
--     order_id	      INT	           PRIMARY KEY,
--     customer_id	      INT	           NOT NULL,
--     restaurant_id	  INT	           NOT NULL,
--     order_amount	  DECIMAL(10,2)	   NOT NULL,
--     order_status	VARCHAR(30)	       NOT NULL,
--     FOREIGN KEY(customer_id)
--     REFERENCES coustomers(customer_id),
--     FOREIGN KEY (restaurant_id)
--     REFERENCES restaurants(restaurant_id)
-- );
-- INSERT INTO coustomers(customer_id,customer_name,email,city) VALUES (
-- 1,	'Rahul',	'rahul@gmail.com'	,'Indore'),
-- (2,	'Priya',	'priya@gmail.com'	,'Bhopal'),
-- (3,	'Aman',	'aman@gmail.com'	,'Indore'),
-- (4,	'Neha',	'neha@gmail.com'	,'Ujjain'),
-- (5,	'Rohan',	'rohan@gmail.com'	,'Indore'
-- );
-- 
-- INSERT INTO restaurants( restaurant_id, restaurant_name,city) VALUES 
--     (101,	'Spice Hub',	'Indore'),
--     (102,	'Food Corner',	'Bhopal'),
--     (103,	'Burger House',	'Indore');
-- SELECT * FROM restaurants;
-- INSERT INTO orders(order_id,customer_id,restaurant_id	,order_amount,order_status)
-- VALUES
-- (1001,	1,	101,	450	,'Delivered'),
-- (1002,	2,	102,	700,	'Delivered'),
-- (1003,	1,	103,	350,	'Pending'),
-- (1004,	3,	101,	550,	'Delivered'),
-- (1005,	5,	103,    900,	'Cancelled');
-- SELECT * FROM orders;
-- CREATE TABLE order_items(item_id	INT	PRIMARY KEY,
-- order_id	INT	NOT NULL,
-- item_name	VARCHAR(100)	NOT NULL,
-- quantity	INT	NOT NULL,
-- FOREIGN KEY (order_id)
-- REFERENCES orders(order_id));
-- SELECT * FROM order_items;
-- INSERT INTO order_items(item_id,order_id,item_name,quantity) VALUES
-- (1,	1001,	'Biryani',	2	),
-- (2,	1001,	'Coke',	2	),
-- (3,	1002,	'Pizza',	1	),
-- (4,	1002,	'Garlic Bread',	1),
-- (5,	1003,	'Burger',	2),
-- (6,	1004,	'Biryani',	1),
-- (7,	1004,	'Coke',	2),
-- (8,	1005,	'Burger',	3);
-- SELECT * FROM order_items;
-- SELECT coustomers customer_name,
-- orders order_id,
-- orders order_status
-- FROM coustomers
-- INNER JOIN orders
-- ON coustomers.customer_id = orders.customer_id;
-- SELECT orders.order_id,
-- restaurants.restaurant_id,
-- orders.order_amount
-- FROM orders
-- INNER JOIN restaurants
-- ON orders.restaurant_id = restaurants.restaurant_id;
SELECT coustomers customer_name,
orders order_id,
orders order_status
FROM coustomers
LEFT JOIN orders
ON coustomers.customer_id = orders.customer_id;

SELECT coustomers.customer_name,
restaurants.restaurant_name,
orders.order_id,
orders.order_amount,
orders order_status
FROM orders
INNER JOIN coustomers
ON orders.customer_id =  coustomers.customer_id
INNER JOIN restaurants
ON orders.restaurant_id = restaurants.restaurant_id;
SELECT coustomers.customer_name,
restaurants.restaurant_name,
orders.order_id,
order_items.item AS item_name,
orders_items.quantity
FROM coustomers 
INNER JOIN orders
ON coustomers.customer_id =  orders.customer_id
INNER JOIN restaurants
ON orders.restaurant_id = restaurants.restaurant_id
INNER JOIN order_items
ON orders.order_id = order_items.order_id;
SELECT coustomers.customer_name,
restaurants.restaurant_name,
orders.order_id,
orders.order_amount
FROM orders
INNER JOIN coustomers
ON orders.customer_id = coutomers.customer_id
INNER JOIN restaurants
ON orders.restaurant_id = restaurants.restaurant_id 
WHERE orders.order_status = 'Delivered';

SELECT coustomers.customer_name,
       orders.order_amount 
FROM coustomers
INNER JOIN orders
ON coustomers.customer_id = orders.customer_id
ORDER BY orders.order_amount DESC;
SELECT coustomers.customer_name,
SUM(orders.order_amount) AS total_order_amount
FROM coustomers
INNER JOIN orders
 ON coustomers.customer_id  = orders.customer_id
GROUP BY coustomers.customer_name;
SELECT coustomers.customer_name,
SUM(orders.order_amount) AS total_order_amount
FROM coustomers
INNER JOIN orders
 ON coustomers.customer_id  = orders.customer_id
GROUP BY coustomers.customer_name
HAVING SUM(orders.order_amount)>600;

SELECT coustomers.customer_name,

orders.order_id,
orders.order_amount
FROM coustomers
INNER JOIN orders
 ON coustomers.customer_id  = orders.customer_id
WHERE coustomers.city = 'Indore';

SELECT coustomers.customer_name,

orders.order_id,
orders.order_amount
FROM coustomers
INNER JOIN orders
 ON coustomers.customer_id  = orders.customer_id
ORDER BY order_amount DESC
LIMIT 1;
SELECT restaurants.resTaurant_name,
SUM(orders.order_amount) AS total_revenue
FROM restaurants
INNER JOIN orders
ON restaurants.restaurant_id = restaurants.restaurant_id 
GROUP BY restaurants.restaurant_name
ORDER BY total_revenue DESC;














