CREATE TABLE students2 (
    students2_id INT PRIMARY KEY,
    students2_name VARCHAR(100),
    age INT,
    course VARCHAR(50),
    marks INT,
    status VARCHAR(20)
);
INSERT INTO students2 (student_id , student_name ,age,course,marks,status)
VALUES
(1,'Rahul',21,'Python',85,'Active'),
(2,'Priya',20,'SQL',92,'Active'),
(3,'Aman',22,'React',78,'Active'),
(4,'Neha',19,'python',65,'Inactive'),
(5,'Rohan',23,'SQL',88,'Active');

SELECT * FROM students2;
# ![alt text](<Screenshot 2026-07-31 201651.png>)

SELECT student_name , course , marks FROM students2;
# ![alt text](<Screenshot 2026-07-31 201818.png>)
 
SELECT * FROM students2 WHERE course = 'Python';
#![alt text](<Screenshot 2026-07-31 202235.png>)

SELECT * FROM students2 WHERE marks > 80;
![alt text](<Screenshot 2026-07-31 202510.png>)

UPDATE students2 SET marks = 90 WHERE student_name = 'Rahul';
![alt text](<Screenshot 2026-07-31 203039.png>)

UPDATE students2 SET status = 'Active' WHERE student_name = 'Neha';
![alt text](<Screenshot 2026-07-31 203128.png>)

DELETE FROM students2 WHERE student_name = 'Aman';


SELECT * FROM students2 WHERE status =  'Active';
![alt text](<Screenshot 2026-07-31 203657.png>)

SELECT * FROM students2;
# ![alt text](<Screenshot 2026-07-31 204252.png>)

