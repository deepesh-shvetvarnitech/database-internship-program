/*                                  SECTION = A


1) SELECT**                                
2) INSERT**                                
3) UPDATE**                                
4) DELETE**                                
5) Filter rows**                          
6) =**                                     
 7) WHERE**                                 
 8) SELECT * FROM students;**               
 9) UPDATE students SET ... WHERE id = 1;** 
10) All rows are deleted**                  
11) ORDER BY**                              
 12) LIMIT**                                 
13) >**                                     
14) LIKE**                                  
15) age BETWEEN 18 AND 22**                 
17) UPDATE**                                
19) SELECT with WHERE** 
18) INSERT                    
20) Create, Read, Update, Delete**  


                                   SECTION = B
                                   QUESTION =1
                                   (A)
SELECT is used to retrieve (read) data from one or more table
(b)
SELECT * FROM students;
(C)
Easy to view all columns.
Helps understand table structure.
PRODUCTION
Retrieves unnecessary columns.
Slower on large tables.
Uses more memory and network bandwidth.
                                QUESTION =2
(A)
It adds a new row (record) into a table.
(B)
INSERT INTO students(name, age, class)
VALUES ('Rahul', 20, 'BCA');

                               QUESTION =3
(A)
It modifies existing records in a table.
(B)
UPDATE students
SET age = 21
WHERE id = 1;
(C)
Without WHERE, every row in the table will be updated
                                QUESTION =4
(A)                                
It removes records (rows) from a table.

(B)
DELETE FROM students
WHERE id = 1;

(C)
DELETE FROM students;
                               QUESTION =5
(A)                               
WHERE filters rows based on a condition.
(B)


Using =

SELECT * FROM students
WHERE age = 20;

Using >

SELECT * FROM students
WHERE age > 18;

Using LIKE

SELECT * FROM students
WHERE name LIKE 'R%'; 

                                    SECTION =C
                                  QUESTION =1
SELECT * FROM students;
                                  QUESTION =2
SELECT name, age, course
FROM students;
                                   QUESTION =3
INSERT INTO students
(student_id, name, age, course, marks, status)
VALUES
(1, 'Aman Kumar', 20, 'Python', 85, 'active');
                                  QUESTION = 4
UPDATE students
SET marks = 90
WHERE name = 'Aman Kumar';
                                  QUESTION =5
DELETE FROM students
WHERE student_id = 5;
                                  QUESTION = 6
SELECT *
FROM students
WHERE age > 18;
                                  QUESTION = 7
SELECT *
FROM students
WHERE course = 'Python'
AND status = 'active';
                                 SECTION =D
                                QUESTION =1
(A)
INSERT INTO students
(student_id, name, age, course, marks, status)
VALUES
(1, 'Aman', 20, 'Python', 85, 'active');

INSERT INTO students
(student_id, name, age, course, marks, status)
VALUES
(2, 'Rahul', 21, 'Java', 78, 'active');

INSERT INTO students
(student_id, name, age, course, marks, status VALUES (3, 'Priya', 19, 'Python', 92, 'inactive');
(B)
SELECT * FROM students;
(C)
UPDATE students SET marks = 95 WHERE student_id = 1;
(D)
DELETE FROM students WHERE student_id = 2;
(E)
SELECT *FROM students WHERE course = 'Python' AND status = 'active';   

                                  QUESTION =2

(A)
INSERT INTO students
(student_id, name, age, course, marks, status)
VALUES
(4, 'Ankit', 18, 'Science', 88, 'active');

(B)
SELECT *
FROM students
WHERE name LIKE 'A%';

(C)
UPDATE students
SET course = 'Mathematics'
WHERE student_id = 4;
*/




                                                            

















