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

