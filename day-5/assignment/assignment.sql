/*
                             SECTION = A
1) GROUP BY
2) HAVING
3) Individual rows before grouping
4) Groups after aggregation
5) SELECT course, COUNT(*) FROM students GROUP BY course;
6) GROUP BY
7) SELECT status, COUNT(*) FROM orders GROUP BY status;
8) ORDER BY
9) SELECT course, COUNT(*) FROM students GROUP BY course;
10) GROUP BY category HAVING COUNT(*) > 5
11) WHERE
12) WHERE
13) HAVING
14) SELECT city, COUNT(*) FROM students GROUP BY city;
15) SELECT course, AVG(marks) FROM students GROUP BY course HAVING AVG(marks) > 80;
16) GROUP BY
17) HAVING
18)Orders per status
19)Filters groups after aggregation
20) Counts by category                             

                              SECTION = B
                             QUESTION =1
                             (A)
GROUP BY groups rows that have the same value into one group.

                               (B)
SELECT course, COUNT(*)
FROM students
GROUP BY course;                 
                                 (C)
It is used for reports such as:

Number of students per course
Orders per status
Sales per city
Employees per department
                                    QUESTION =2.
                                    (A) 

HAVING filters groups after they are created.

It is mainly used with aggregate functions.
                                     (B)
Difference from WHERE
WHERE	HAVING
Filters rows	Filters groups
Runs before GROUP BY	Runs after GROUP BY
Cannot use COUNT() directly	Can use COUNT(), AVG(), SUM()

                                       (C)
SELECT course, COUNT(*)
FROM students
GROUP BY course
HAVING COUNT(*) > 5;
                               QUESTION = 3
                               (A)
COUNT() counts the number of rows.
                                  
Example:

SELECT course, COUNT(*)
FROM students
GROUP BY course;

Output

Course	Count
Python	12
SQL	15
Java	8

                                           QUESTION =4                      
Example (E-Commerce)
SELECT status, COUNT(*)
FROM orders
GROUP BY status;

Output

Status	Orders
Delivered	250
Pending	40
Cancelled	15

                                     QUESTION = 5
WHERE	                                          HAVING
Filters individual rows                        	Filters grouped data
Executes before grouping   	                    Executes after grouping
Doesn't work on aggregate results	            Works on aggregate results


                                       (B)

SELECT *
FROM students
WHERE age > 18;


                                    SECTION = C

                                     QUESTION =1


SELECT course, COUNT(*) AS total_students
FROM students
GROUP BY course;
                                    QUESTION = 2. 
                                    Count Students by City

SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city;

                                    QUESTION = 3 
                                    
                                 Average Marks by Course

SELECT course, AVG(marks) AS average_marks
FROM students
GROUP BY course;
                                     QUESTION =4. 
                                Courses with More Than 2 Students
SELECT course, COUNT(*) AS total_students
FROM students
GROUP BY course
HAVING COUNT(*) > 2;
                                     QUESTION = 5.
                                Cities with More Than 3 Students
SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city
HAVING COUNT(*) > 3;

                                    QUESTION = 6 
                                 Completed Status Count
SELECT status, COUNT(*) AS total_students
FROM students
GROUP BY status;
                                    QUESTION = 7 
                                Average Marks Above 75
SELECT course, AVG(marks) AS average_marks
FROM students
GROUP BY course
HAVING AVG(marks) > 75;

                                     Section D

                                     QUESTION = 1
                                     (A)
SELECT course
FROM students
GROUP BY course;
Courses with more than 5 students

(B)
SELECT course
FROM students
GROUP BY course
HAVING COUNT(*) > 5;
Average marks per course

(C)
SELECT course
FROM students
GROUP BY course;
Courses with average marks above 70

(D)
SELECT course
FROM students
GROUP BY course
HAVING AVG(marks) > 70     

                                     QUESTION = 2
(A)  
orders(
    order_id INT,
    customer_name VARCHAR(100),
    status VARCHAR(30),
    amount DECIMAL(10,2)
);
(B)
SELECT status
FROM orders
GROUP BY status;
(C)
SELECT status
FROM orders
GROUP BY status
HAVING COUNT(*) > 20;
(D)
SELECT status
FROM orders
GROUP BY status;

(E)
SELECT status
FROM orders
GROUP BY status
HAVING AVG(amount) > 500;                                   
*/

                                            


                             