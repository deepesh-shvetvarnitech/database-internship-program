/*                       
                             Section A 



1) JOIN
2) Only matching rows from both tables
3) All rows from left table and matching rows from right table
4) LEFT JOIN
5) INNER JOIN
6) NULL
7) SELECT * FROM users JOIN orders ON users.user_id = orders.user_ida) Two JOIN clauses
8) ON
9) Matching user_id in both tables
10) LEFT JOIN
11 INNER JOIN
12 Query data across multiple related tables
13 2
14 SELECT * FROM products LEFT JOIN order_items ON products.product_id = order_items.product_ida) The join condition
15) INNER JOIN and LEFT JOIN
16) orders, customers, products, order_items
17) All users, including those without orders
18) It requires matching values in both tables





                              SECTION =B
                              QUESTION =1
  (A)
  INNER JOIN do tables ko connect karta hai aur sirf wahi records return karta hai jinka matching data dono tables mein hota hai.
                                       (B)
Example:

SELECT users.name, orders.order_id, orders.amount
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id;  
                            QUESTION = 2
                                   (A)
LEFT JOIN returns all rows from the left table and the matching rows from the right table.

If there is no matching record in the right table, SQL returns NULL for the right table's columns.
                                   (B)
Example:
SELECT users.name, orders.order_id, orders.amount
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id;

This query displays all users, including users who have not placed any orders.

                                     (C)
 LEFT JOIN useful 

LEFT JOIN is useful when we need a complete list of records, including records that do not have related data.

Example:
"Show all users and their orders, including users who have never ordered."   


                          QUESTION = 3
                             (A)
 The main difference is how they handle non-matching records.
                             (B)
INNER JOIN	                               LEFT JOIN
Returns only matching rows	              Returns all rows from the left table
Non-matching rows are excluded	          Non-matching left rows are included
No NULL rows for unmatched records	      Right-side columns become NULL when there is no match
                                   (C)
INNER JOIN:
SELECT users.name, orders.order_id
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id;     

LEFT JOIN:
SELECT users.name, orders.order_id
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id;
                                               question = 4
                                                (A)
A multi-table JOIN is used when we need to retrieve data from three or more related tables.
                                                (B)
For example, suppose we have:

customers
    ↓
orders
    ↓
products

We can join all three tables using their related IDs.

Example:
SELECT
    orders.order_id,
    customers.name AS customer_name,
    products.name AS product_name,
    orders.amount
FROM orders
INNER JOIN customers
ON orders.user_id = customers.user_id
INNER JOIN products
ON orders.product_id = products.product_id;   

                                           Question = 5
Joins are commonly used in e-commerce and CRM systems.
                                        (B)
Example 1 — E-Commerce

An e-commerce application may have:

customers
orders
products
                                                   (C)
Using JOINs, we can retrieve:

Customer name
Order ID
Product name
Product price
Order amount

Example:

SELECT
    customers.name,
    orders.order_id,
    products.name AS product_name,
    products.price
FROM orders
INNER JOIN customers
ON orders.user_id = customers.user_id
INNER JOIN products
ON orders.product_id = products.product_id;                                                                                      

                                                 SECTION = C
                                                QUESTION = 1
SELECT DISTINCT
    users.user_id,
    users.name,
    users.email
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id;

                                               QUESTION =2


SELECT
    users.user_id,
    users.name,
    orders.order_id,
    orders.amount
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id;

                                                    QUESTION =3


SELECT
    orders.order_id,
    orders.quantity,
    orders.amount,
    orders.order_date,
    users.name,
    users.email
FROM orders
INNER JOIN users
ON orders.user_id = users.user_id;


                                                   QUESTION = 4


SELECT
    orders.order_id,
    orders.quantity,
    orders.amount,
    orders.order_date,
    products.name AS product_name,
    products.price
FROM orders
INNER JOIN products
ON orders.product_id = products.product_id;

                                                QUESTION = 5

SELECT
    orders.order_id,
    users.name AS customer_name,
    users.email,
    products.name AS product_name,
    products.price,
    orders.quantity,
    orders.amount,
    orders.order_date
FROM orders
INNER JOIN users
ON orders.user_id = users.user_id
INNER JOIN products
ON orders.product_id = products.product_id;
Tables joined:
orders
   ↓
users

orders
   ↓
products

                                                QUESTION = 6

Answer:
SELECT
    orders.order_id,
    users.name AS customer_name,
    users.email,
    products.name AS product_name,
    products.price,
    orders.quantity,
    orders.amount
FROM orders
INNER JOIN users
ON orders.user_id = users.user_id
INNER JOIN products
ON orders.product_id = products.product_id
WHERE orders.amount > 1000;
Important:

JOIN connects the tables.

WHERE filters the result.

So the order is:

FROM
↓
JOIN
↓
JOIN
↓
WHERE
↓
SELECT result
                                         QUESTION =7
SELECT
    users.user_id,
    users.name,
    COUNT(orders.order_id) AS total_orders
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id
GROUP BY
    users.user_id,
    users.name;                                                
                                          SECTION =D
                                         QUESTION =1
SELECT
    orders.order_id,
    users.name AS customer_name,
    users.email,
    products.name AS product_name,
    orders.quantity,
    orders.amount,
    orders.order_date
FROM orders
INNER JOIN users
ON orders.user_id = users.user_id
INNER JOIN products
ON orders.product_id = products.product_id;

                                            QUESTION = B
SELECT
    users.user_id,
    users.name,
    users.email,
    orders.order_id,
    orders.amount,
    orders.order_date
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id;
                                                     C            
SELECT
    users.user_id,
    users.name,
    SUM(orders.amount) AS total_order_amount
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id
GROUP BY
    users.user_id,
    users.name;
                                                       D 
SELECT
    users.user_id,
    users.name,
    SUM(orders.amount) AS total_order_amount
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id
GROUP BY
    users.user_id,
    users.name
ORDER BY total_order_amount DESC
LIMIT 1;
                                           QUESTION =2
                                           (A)
SELECT
    orders.order_id,
    orders.product_id,
    orders.quantity,
    orders.amount,
    orders.order_date
FROM orders
WHERE orders.user_id = 5
ORDER BY orders.order_date DESC;
                                               B
SELECT
    products.name AS product_name,
    products.price,
    orders.quantity,
    orders.order_date
FROM orders
INNER JOIN products
ON orders.product_id = products.product_id
WHERE orders.user_id = 5
ORDER BY orders.order_date DESC;
                                                 C   
SELECT
    users.user_id,
    users.name,
    SUM(orders.amount) AS total_spending
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id
GROUP BY
    users.user_id,
    users.name;
                                             D 
SELECT
    users.user_id,
    users.name,
    users.email
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id
WHERE orders.order_id IS NULL;










