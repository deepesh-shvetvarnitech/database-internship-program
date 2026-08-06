/*                                section =A 

1) SELECT
2) WHERE
3) ORDER BY
4) DISTINCT
5) SUM
6) COUNT
7) GROUP BY
8) HAVING
9) LIKE
10) IN
11) BETWEEN
12) Returns only 5 rows
13) SELECT * FROM students ORDER BY marks DESC LIMIT 3;
14) SELECT DISTINCT course FROM students;
15) WHERE
16) SELECT course, COUNT(*) FROM students GROUP BY course;
17) GROUP BY course HAVING COUNT(*) > 2
18) INSERT
19) UPDATE
20) DELETE
                              section =B
                              question =1
                              (A)
WHERE	                                      HAVING
Filters individual rows.	                  Filters groups.
Used before GROUP BY.	                       Used after GROUP BY.
Cannot use aggregate functions like COUNT().  an use aggregate functions.

                                   (B)

SELECT * FROM students
WHERE marks > 70;

SELECT course, COUNT(*)
FROM students
GROUP BY course
HAVING COUNT(*) > 2;
                                    QUESTION = 2


DISTINCT removes duplicate values from the result.

It helps to:

Show unique courses
Show unique cities
Avoid repeated values in reports


                                         (b)

SELECT DISTINCT course
FROM students;

3


Counts the number of rows.

SELECT COUNT(*)
FROM students;
SUM()

Adds all numeric values.

SELECT SUM(marks)
FROM students;
AVG()

Calculates the average.

SELECT AVG(marks)
FROM students;

                                     QUESTION = 4


ORDER BY sorts the data.

LIMIT returns only the required number of rows.

                                      (b)
SELECT *
FROM students
ORDER BY marks DESC
LIMIT 5;

                                        QUESTION = 5


GROUP BY combines rows having the same value into one group.


                                        (B)

Students in each course
Employees in each department
Sales per city

Example

SELECT course, COUNT(*)
FROM students
GROUP BY course;            
           
Section C

                                        QUESTION = 1

SELECT *
FROM students
ORDER BY marks DESC;
                                      QUESTION = 2

SELECT *
FROM students
ORDER BY marks DESC
LIMIT 5;

                                    QUESTION = 3

SELECT DISTINCT course
FROM students;

                                     QUESTION = 4

SELECT *
FROM students
WHERE name LIKE 'A%';

                                      QUESTION = 5

SELECT *
FROM students
WHERE city IN ('Delhi', 'Bhopal', 'Indore');

                                      QUESTION = 6

SELECT *
FROM students
WHERE marks BETWEEN 60 AND 80;

                                    QUESTION = 7

SELECT COUNT(*)
FROM students;

                                    QUESTION = 8

SELECT AVG(marks)
FROM students;

                                      QUESTION = 9

SELECT course, COUNT(*)
FROM students
GROUP BY course;

                                       QUESTION = 10

SELECT course, COUNT(*)
FROM students
GROUP BY course
HAVING COUNT(*) > 3;   


                                       SECTION = D
                                    QUESTION = 1
CREATE TABLE book_sales (
    sale_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    book_title VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    payment_method VARCHAR(30) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    order_status VARCHAR(20) NOT NULL
);

INSERT INTO book_sales
(sale_id, customer_name, book_title, category, payment_method, amount, order_status)
VALUES
(1, 'Rahul', 'Python Basics', 'Programming', 'UPI', 650.00, 'Completed'),
(2, 'Priya', 'SQL Mastery', 'Programming', 'Card', 750.00, 'Completed'),
(3, 'Aman', 'Atomic Habits', 'Self Help', 'UPI', 500.00, 'Completed'),
(4, 'Neha', 'Rich Dad Poor Dad', 'Finance', 'Cash', 450.00, 'Cancelled'),
(5, 'Rohan', 'React Guide', 'Programming', 'Card', 900.00, 'Completed'),
(6, 'Anjali', 'Think and Grow Rich', 'Finance', 'UPI', 600.00, 'Completed'),
(7, 'Karan', 'Clean Code', 'Programming', 'Card', 1200.00, 'Pending'),
(8, 'Sneha', 'Deep Work', 'Self Help', 'UPI', 700.00, 'Completed'),
(9, 'Vikas', 'Python Advanced', 'Programming', 'Cash', 1500.00, 'Completed'),
(10, 'Pooja', 'The Psychology of Money', 'Finance', 'Card', 850.00, 'Completed'),
(11, 'Arjun', 'SQL Interview Guide', 'Programming', 'UPI', 950.00, 'Completed'),
(12, 'Nisha', 'Ikigai', 'Self Help', 'Cash', 550.00, 'Completed');

SELECT * FROM book_sales;

SELECT customer_name, book_title, amount
FROM book_sales;

SELECT *
FROM book_sales
WHERE order_status = 'Completed';

SELECT *
FROM book_sales
WHERE category IN ('Programming', 'Finance');



SELECT *
FROM book_sales
WHERE customer_name LIKE 'A%';


SELECT *
FROM book_sales
WHERE amount BETWEEN 600 AND 1000;


SELECT *
FROM book_sales
ORDER BY amount DESC;


SELECT *
FROM book_sales
ORDER BY amount DESC
LIMIT 5;


SELECT DISTINCT payment_method
FROM book_sales;


UPDATE book_sales
SET order_status = 'Completed'
WHERE book_title = 'Clean Code';


DELETE FROM book_sales
WHERE order_status = 'Cancelled';


SELECT *
FROM book_sales
WHERE order_status = 'Completed';


SELECT COUNT(*) AS total_sales
FROM book_sales;


SELECT SUM(amount) AS total_revenue
FROM book_sales
WHERE order_status = 'Completed';


SELECT AVG(amount) AS average_sale
FROM book_sales;


SELECT MAX(amount) AS highest_sale
FROM book_sales;


SELECT MIN(amount) AS lowest_sale
FROM book_sales;


SELECT category, COUNT(*) AS books_sold
FROM book_sales
GROUP BY category;


SELECT payment_method, SUM(amount) AS total_revenue
FROM book_sales
GROUP BY payment_method;


SELECT category, AVG(amount) AS average_sale
FROM book_sales
GROUP BY category
HAVING AVG(amount) > 700;


SELECT payment_method, SUM(amount) AS total_revenue
FROM book_sales
GROUP BY payment_method
HAVING SUM(amount) > 2000;


SELECT *
FROM book_sales
ORDER BY category ASC, amount DESC;
Bonus Challenge 1




SELECT *
FROM book_sales
WHERE book_title LIKE '%Python%';






SELECT category, AVG(amount) AS average_sale
FROM book_sales
GROUP BY category
ORDER BY average_sale DESC
LIMIT 1;
Bonus Challenge 3




SELECT payment_method, COUNT(*) AS completed_orders
FROM book_sales
WHERE order_status = 'Completed'
GROUP BY payment_method
HAVING COUNT(*) > 3;
Bonus Challenge 4




SELECT category, SUM(amount) AS total_revenue
FROM book_sales
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 2;

                                     QUESTION = 2


CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50) NOT NULL
);


CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    order_amount DECIMAL(10,2) NOT NULL,
    order_status VARCHAR(20) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


INSERT INTO customers
(customer_id, customer_name, email, city)
VALUES
(1, 'Rahul', 'rahul@gmail.com', 'Indore'),
(2, 'Priya', 'priya@gmail.com', 'Bhopal'),
(3, 'Aman', 'aman@gmail.com', 'Ujjain'),
(4, 'Neha', 'neha@gmail.com', 'Indore'),
(5, 'Rohan', 'rohan@gmail.com', 'Bhopal'),
(6, 'Anjali', 'anjali@gmail.com', 'Ujjain');


INSERT INTO orders
(order_id, customer_id, product_name, category, order_amount, order_status)
VALUES
(101, 1, 'Laptop', 'Electronics', 65000, 'Delivered'),
(102, 2, 'Keyboard', 'Electronics', 1500, 'Delivered'),
(103, 3, 'Office Chair', 'Furniture', 8500, 'Pending'),
(104, 1, 'Mouse', 'Electronics', 900, 'Delivered'),
(105, 4, 'Study Table', 'Furniture', 12000, 'Delivered'),
(106, 5, 'Monitor', 'Electronics', 18000, 'Cancelled'),
(107, 2, 'Notebook Pack', 'Stationery', 400, 'Delivered'),
(108, 6, 'Printer', 'Electronics', 14000, 'Delivered'),
(109, 4, 'Desk Lamp', 'Furniture', 2500, 'Pending'),
(110, 5, 'Pen Set', 'Stationery', 350, 'Delivered');


SELECT * FROM customers;


SELECT * FROM orders;


SELECT product_name, category, order_amount
FROM orders;


SELECT *
FROM orders
WHERE order_status = 'Delivered';


SELECT *
FROM orders
WHERE category IN ('Electronics', 'Furniture');


SELECT *
FROM customers
WHERE customer_name LIKE 'R%';


SELECT *
FROM orders
WHERE order_amount BETWEEN 1000 AND 20000;


SELECT *
FROM orders
ORDER BY order_amount DESC
LIMIT 5;


SELECT DISTINCT category
FROM orders;


UPDATE orders
SET order_status = 'Delivered'
WHERE product_name = 'Office Chair';


DELETE FROM orders
WHERE order_status = 'Cancelled';


SELECT COUNT(*) AS total_orders
FROM orders;


SELECT SUM(order_amount) AS total_revenue
FROM orders
WHERE order_status = 'Delivered';


SELECT AVG(order_amount) AS average_order
FROM orders;


SELECT MAX(order_amount) AS highest_order
FROM orders;


SELECT MIN(order_amount) AS lowest_order
FROM orders;


SELECT category, COUNT(*) AS total_orders
FROM orders
GROUP BY category;


SELECT category, SUM(order_amount) AS total_revenue
FROM orders
GROUP BY category;


SELECT category, COUNT(*) AS total_orders
FROM orders
GROUP BY category
HAVING COUNT(*) > 2;


SELECT category, SUM(order_amount) AS total_revenue
FROM orders
GROUP BY category
HAVING SUM(order_amount) > 20000;


SELECT *
FROM orders
ORDER BY category ASC, order_amount DESC;


SELECT category, COUNT(*) AS delivered_orders
FROM orders
WHERE order_status = 'Delivered'
GROUP BY category;


SELECT city, COUNT(*) AS total_customers
FROM customers
GROUP BY city
HAVING COUNT(*) > 1;


SELECT category, AVG(order_amount) AS average_order
FROM orders
GROUP BY category
HAVING AVG(order_amount) > 10000;


SELECT category, SUM(order_amount) AS total_revenue
FROM orders
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 2;                                     