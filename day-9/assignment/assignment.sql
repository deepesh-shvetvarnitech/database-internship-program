/*                                     SECTION = A

1	A query inside another query
2	Inner query or nested query
3	Parentheses
4	All of the above
5	Scalar subquery
6	Multi-row subquery
7	IN
8   References columns from outer query
9	price < (SELECT AVG(price)...)
10	First query
11	SELECT, INSERT, UPDATE, DELETE
12	They can be nested inside other subqueries
13	Add a calculated column
14	price = (SELECT MAX(price)...)
15	Perform operations in multiple steps
16	Both IN and EXISTS
17	Correlated subquery
18	user_id IN (SELECT user_id FROM orders)
19	Some JOIN operations
20	Break complex queries into logical steps

                                         SECTION = B
                                         QUESTION = 1
                                         A
A subquery is a query written inside another SQL query.

                                           B

SELECT *
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);

Here:

SELECT AVG(price) FROM products

is the subquery, and the outer SELECT uses its result.
                                                         C
useful

Subqueries are useful when we need to perform a task in multiple logical steps.      

                                            QUESTION = 2
                                            A
Returns exactly one value.
                                            B
Example:

SELECT *
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);

AVG(price) returns one value.

Example result:

Average = 2500

So outer query becomes conceptually:

SELECT *
FROM products
WHERE price > 2500;
                                                       B
Multi-Row Subquery

Returns multiple rows.

Example:

SELECT *
FROM users
WHERE user_id IN (
    SELECT user_id
    FROM orders
);                                            
                                              QUESTION = 3
                                                A 
Returns exactly one value.

Example:

SELECT *
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);

AVG(price) returns one value.

Example result:

Average = 2500

So outer query becomes conceptually:

SELECT *
FROM products
WHERE price > 2500;
Multi-Row Subquery

Returns multiple rows.

Example:

SELECT *
FROM users
WHERE user_id IN (
    SELECT user_id
    FROM orders
);                
                                      QUESTION = 4
                                          (A)
Subqueries are very useful with aggregate functions:

AVG()
MAX()
MIN()
SUM()
COUNT()
                                                        B
Example: Above-average products
SELECT *
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);               
                                               SECTION = C
                                              QUESTION = 1

Q1


SELECT u.user_id, u.name, SUM(o.amount) AS total_spending
FROM users u
JOIN orders o
    ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
HAVING SUM(o.amount) > (
    SELECT AVG(total_spending)
    FROM (
        SELECT SUM(amount) AS total_spending
        FROM orders
        GROUP BY user_id
    ) AS spending
);

Q2
SELECT *
FROM products
WHERE price < (
    SELECT AVG(price)
    FROM products
);


Q3



SELECT *
FROM products
WHERE stock_quantity < 10;

Q4
SELECT *
FROM products
WHERE price = (
    SELECT MAX(price)
    FROM products
);

WHERE price = (
    SELECT MAX(price)
    FROM products
);
Q5
SELECT *
FROM users
WHERE user_id IN (
    SELECT user_id
    FROM orders
);

Inner query:

SELECT user_id
FROM orders;


Q6
SELECT *
FROM users
WHERE user_id NOT IN (
    SELECT user_id
    FROM orders
);



Q


Q6

User does not exist in orders.

Practical note: In production SQL, NOT EXISTS is often safer than NOT IN when the subquery could contain NULL.

Q7
SELECT *
FROM products
WHERE category IN (
    SELECT category
    FROM products
    WHERE price > 1000
);
Logic

                                          SECTION = D
                                          QUESTION =1
                                          
A

SELECT
    user_id,
    SUM(amount) AS total_spending
FROM orders
GROUP BY user_id;
                                                          B
SELECT u.user_id, u.name, SUM(o.amount) AS total_spending
FROM users u
JOIN orders o
    ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
HAVING SUM(o.amount) > (
    SELECT AVG(total_spending)
    FROM (
        SELECT SUM(amount) AS total_spending
        FROM orders
        GROUP BY user_id
    ) AS spending
);
                                                        C
SELECT u.user_id, u.name, SUM(o.amount) AS total_spending
FROM users u
JOIN orders o
    ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
HAVING SUM(o.amount) = (
    SELECT MAX(total_spending)
    FROM (
        SELECT SUM(amount) AS total_spending
        FROM orders
        GROUP BY user_id
    ) AS spending
);



                                                    D
SELECT *
FROM users
WHERE user_id NOT IN (
    SELECT user_id
    FROM orders
);

                                                    QUESTION =2
                                                          A
SELECT *
FROM products
WHERE stock_quantity < (
    SELECT AVG(stock_quantity)
    FROM products
);
                                                             B
SELECT *
FROM products
WHERE category IN (
    SELECT category
    FROM products
    GROUP BY category
    HAVING AVG(price) > 500
);
Logic

Inner query:

SELECT category
FROM products
GROUP BY category
HAVING AVG(price) > 500;

Finds qualifying categories.

Outer query:

SELECT *
FROM products
WHERE category IN (...);

finds all products from those categories.

                                                            C



SELECT p1.*
FROM products p1
WHERE p1.price = (
    SELECT MIN(p2.price)
    FROM products p2
    WHERE p2.category = p1.category
);                                                   