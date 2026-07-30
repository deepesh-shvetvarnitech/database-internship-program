CREATE DATABASE training_center:

USE training_center:
CREATE TABLE students{
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15) NULL,
    city VARCHAR(50) NULL
};
CREATE TABLE courses {
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    duration VARCHAR(30) NOT NULL

};
CREATE TABLE enrollments{
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY(student_id) REFRENCES student(student_id),
    FOREIGN KEY(course_id) REFRENCES course(course_id)

};
INSERT INTO students(student_id,student_name,email,phone,city)
VALUES
(1,'Rahul','rahul@gmail.com','9876543210','INDORE');
(2,'Priya','navin@gmail.com',NULL,'BHOPAL');
(3,'Aman','aman@gmail.com','9123456789','ujjain');
INSERT INTO courses(course_id,course_name,duration)
VALUES
(101,'python','2months');
(102,'SQL','1months');
(103,'react','2months');
INSERT INTO enrollments(enrollment_id,student_id,course_id)
(1,1,101);
(2,2,102);
(3,3,103);
SELECT*FROM students;
SELECT*FROM courses;
SELECT*FROM enrollments;
SELECT 
     students.students_name,
     course.course_name,
FROM enrollments
JOIN students
ON enrollments.student_id = student.student_id
JOIN courses
ON enrollments.course_id = course.course_id;

--student_id in students table is the primary key
--course_id in course table is the primary key
--enrollment_id in enrollment table is the primary key
--student_id in enrollment table is the forign key
--course_id in students table is the forign key
--phone column in students table allows NULL values
--city column in students table allows NULL values
--email colummn is UNIQUE

SELECT*FROM students WHERE phone is NULL;
SELECT * FROM students WHERE email = 'rahul@gmail.com';











