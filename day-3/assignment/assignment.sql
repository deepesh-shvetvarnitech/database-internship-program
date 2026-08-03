--                            section = a
/*
1 (ORDER BY)
2 (Ascending order)
3 (LIMIT)
4 (DISTINCT)
5 (LIKE)
6 (%)
7 (_)
8 (IN)
9 (BETWEEN)
10 (10 and 20 also)
11(ORDER BY marks DESC)
12(SELECT * FROM students ORDER BY marks DESC LIMIT 5;)
13(DISTINCT)
14(name LIKE 'A%')
15(name LIKE '%an%')
16(age IN (18, 19, 20))
17(marks BETWEEN 70 AND 90)
18(ORDER BY name ASC)
19(DISTINCT)
20 (ORDER BY and LIMIT)

                              SECTION = B
                              QUESTION = 1
                              (A)
ORDER BY is used to sort the result of a query.
It can sort data in ascending (ASC) or descending (DESC) order.
                              (B)
SELECT * FROM students
ORDER BY marks DESC;
                               (C)
Makes reports easier to read.
Helps show highest or lowest values first.
                             QUESTION =2
                             (A)
LIMIT returns only a fixed number of rows
                              (B)
SELECT * FROM students
ORDER BY marks DESC
LIMIT 3;
                             (C)
Displays only top records.
Improves dashboard and API performance.
                              QUESTION =3
                              (A)
DISTINCT removes duplicate values from the result.
(B)
SELECT DISTINCT course
FROM students;
(C)
Many students can belong to the same course.

QUESTION =4
(A)
LIKE is used to search text patterns.
(B)
SELECT *
FROM students
WHERE name LIKE 'A%';
SELECT *
FROM students
WHERE name LIKE '_an';

QUESTION =5
(A)
Checks whether a value exists in a list.
SELECT *
FROM students
WHERE city IN ('Delhi','Indore','Bhopal');

BETWEEN

Checks whether a value lies within a range.
SELECT * FROM students WHERE marks BETWEEN 60 AND 80;

                                   SECTION =C
1)
SELECT * FROM students ORDER BY marks DESC;
2)
SELECT * FROM students ORDER BY marks DESC LIMIT 5;
3. 
SELECT DISTINCT course FROM students;
4.
SELECT * FROM students WHERE name LIKE 'A%';
5
SELECT * FROM students WHERE name LIKE '%an%';
6.
SELECT * FROM students WHERE city IN ('Delhi','Bhopal','Indore');
7
SELECT * FROM students WHERE marks BETWEEN 60 AND 80;

                                       SECTION =D
                                       QUESTION =1
SELECT *
FROM students
ORDER BY marks DESC
LIMIT 10;
                                        Unique Courses
SELECT DISTINCT course
FROM students;
                                    Names Starting with S
SELECT *
FROM students
WHERE name LIKE 'S%';
                                    Marks Between 75 and 90
SELECT *
FROM students
WHERE marks BETWEEN 75 AND 90;                                                              

                                    QUESTION =2
                           Students from Selected Cities
SELECT *
FROM students
WHERE city IN ('Delhi','Indore','Bhopal');
                                 Names Containing "ar"
SELECT *
FROM students
WHERE name LIKE '%ar%';
                                    Sort by Age
SELECT *
FROM students
ORDER BY age ASC;
                                Show First 5 Results
SELECT *
FROM students
LIMIT 5;                                    












































































































































































































































































































































































*/