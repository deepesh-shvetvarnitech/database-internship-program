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