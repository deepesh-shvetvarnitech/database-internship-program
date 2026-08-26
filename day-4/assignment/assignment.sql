/*
                                section=a
1— COUNT
2 — SUM
3 — AVG
4 — MIN
5 — MAX
6 — Summarize data
7 — SELECT COUNT(*) FROM orders;
8 — SUM
9 — MAX
10 — MIN
11 — AVG
12 — GROUP BY
13 — SELECT COUNT(order_id) FROM orders;
14 — SELECT SUM(amount) FROM orders;
15 — SELECT AVG(price) FROM products;
16 — SELECT MIN(marks) FROM students;
17 — SELECT MAX(marks) FROM students;
18 — COUNT(column_name)
19 — Daily sales report
20 — Totals, averages, and trends 

                            SECTION =B
                              QUESTION =1
(A)
COUNT() is used to count the number of rows (records) in a table.

(B)

SELECT COUNT(*) FROM orders;    

(C)
Counts total orders
Counts total customers
Counts total products
Helps generate summary reports
                                   QUESTION =2
SUM() is used to calculate the total of a numeric column.

(B)

SELECT SUM(amount) FROM orders;

(C)

Total sales
Total revenue
Total salary
Total expenses 
                                    QUESTION =3
(A)
AVG() calculates the average value of a numeric column.


(B)
SELECT AVG(amount) FROM orders;





(C)

Shows average order value
Shows average student marks
Shows average salary
Helps analyze overall performance 

                                QUESTION =4
(A)                                
MIN() returns the smallest value in a column.
(B)


SELECT MIN(amount) FROM orders;

MAX() returns the largest value in a column.



SELECT MAX(amount) FROM orders;

(C)
Difference:

MIN() → Returns the smallest value.
MAX() → Returns the largest value.                                

                                 QUESTION =5
(A)
Aggregate functions are important in backend systems because they summarize data and generate reports for analysis.

(B)

E-Commerce
Total Orders → COUNT()
Total Revenue → SUM(amount)

Student Reports
Average Marks → AVG(marks)
Highest Marks → MAX(marks)

                            SECTION = C


                           QUESTION =1

SELECT COUNT(*) AS total_orders
FROM orders;
                                    QUESTION = 2 




SELECT SUM(amount) AS total_sales
FROM orders;
                                
                                QUESTION = 3.





SELECT AVG(amount) AS average_order_value
FROM orders;

                               QUESTION = 4. 
                               


SELECT MIN(amount) AS minimum_order_amount
FROM orders;

                                   QUESTION = 5




SELECT MAX(amount) AS maximum_order_amount
FROM orders;
                                      QUESTION = 6



SELECT COUNT(*) AS completed_orders
FROM orders
WHERE status = 'completed';
                               QUESTION =7



SELECT AVG(quantity) AS average_quantity
FROM orders;    

                                  SECTION = D
                                  QUESTION =1


a) 

SELECT COUNT(*) AS total_orders
FROM orders;
b) 

SELECT SUM(amount) AS total_revenue
FROM orders;
c)

SELECT AVG(amount) AS average_order_value
FROM orderd
d) 

SELECT MIN(amount) AS minimum_order_amount,
       MAX(amount) AS maximum_order_amount
FROM orders;    

                            QUESTION =2

a)
SELECT COUNT(*) AS completed_orders
FROM orders
WHERE status = 'completed';
b) 

SELECT SUM(quantity) AS total_quantity_sold
FROM orders;
c) 

SELECT AVG(quantity) AS average_quantity_per_order
FROM orders;
d) 

SELECT MIN(amount) AS minimum_order_amount,
       MAX(amount) AS maximum_order_amount
FROM orders;                            
*/