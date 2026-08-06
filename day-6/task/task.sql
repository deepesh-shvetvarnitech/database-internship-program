CREATE TABLE employees(
    employee_id	INT	PRIMARY KEY,
    employee_name	VARCHAR(100)	NOT NULL,
    email	        VARCHAR(100) UNIQUE,
    
    department	    VARCHAR(50)	    NOT NULL,
    salary	        DECIMAL(10,2)	NOT NULL
);
DROP TABLE employees;
CREATE TABLE employees(
    employee_id	INT	PRIMARY KEY,
    employee_name	VARCHAR(100)	NOT NULL,
    email	        VARCHAR(100) UNIQUE,
    
    department	    VARCHAR(50)	    NOT NULL,
    salary	        DECIMAL(10,2)	NOT NULL
);
CREATE TABLE leave_requests(
    leave_id	INT	PRIMARY KEY,
    employee_id	INT	,
    leave_type	VARCHAR(30)	NOT NULL,
    leave_days	INT	NOT NULL,
    leave_status	VARCHAR(20)	NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
-- INSERT INTO employees (employee_id	,employee_name,email,department,salary)
-- VALUES
-- (1,	'Rahul','Rahul@gmail.com',	'Engineering',	60000),
-- (2,	'Priya','Priya@gmail.com',	'HR',	45000),
-- (3,	'Aman','Aman@gmail.com'	,'Engineering',	70000),
-- (4,	'Neha','Neha@gmail.com'	,'Finance',	55000),
-- (5,	'Rohan','Rohan@gmail.com',	'Marketing',	50000),
-- (6,	'Anjali','Anjali@gmail.com',	'Engineering',	65000),
-- (7,	'Karan','Karan@gmail.com',	'Finance',	58000),
-- (8,	'Sneha','Sneha@gmail.com',	'HR',	47000);

-- INSERT INTO leave_requests(leave_id,employee_id,leave_type,leave_days,leave_status)
-- VALUES
-- (101,	1,	'Sick',	2,	'Approved'),
-- (03,	3,	'Annual',	5,	'Pending'),
-- (104,	4,	'Sick',	3,	'Approved'),
-- (105,	5,	'Annual',	4,	'Rejected'),
-- (106,	6,	'Casual',	2,	'Approved'),
-- (107,	7,	'Sick',	1,	'Pending'),
-- (108,	8,	'Annual',	6,	'Approved'),
-- (109,    1,	'Annual',	3,	'Approved'),
-- (110,	3,	'Casual',	2,	'Approved'),
-- (111,	5,	'Sick',	1,	'Approved'),
-- (112,	6,	'Annual',	4,	'Pending');
-- SELECT  * FROM  employees;
-- SELECT * FROM leave_requests;
-- SELECT employee_name,department,salary FROM employees;
-- SELECT  * FROM  employees WHERE department IN ('Engineering','Finance');
 SELECT  * FROM  employees WHERE employee_name LIKE 'A%';
 SELECT  * FROM  employees WHERE salary BETWEEN 50000 AND 65000;
 SELECT  * FROM  employees ORDER BY salary DESC;
 SELECT  * FROM  employees ORDER BY salary DESC LIMIT 5;
 SELECT DISTINCT department FROM employees;
 
 UPDATE leave_requests SET leave_status = 'Approved' WHERE employee_id = 3 AND leave_type = 'Annual'AND leave_status = 'Pending';
 DELETE FROM leave_requests WHERE leave_status = 'Pending';
SELECT * FROM leave_requests WHERE leave_status = 'Approved';
SELECT COUNT(*)AS total_leave_requests FROM leave_requests;
SELECT COUNT(*)AS total_employees FROM employees;
SELECT SUM(leave_days) AS total_approved_leave_days FROM leave_requests;
SELECT AVG(salary) AS average_salary FROM employees;
SELECT MAX(salary) AS highest_salary FROM employees;
SELECT MIN(salary) AS lowest_salary FROM employees;
SELECT department, COUNT(*) AS employees FROM employees GROUP BY department;
SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department;
SELECT department, AVG(salary) AS total_salary FROM employees GROUP BY department;
SELECT department, COUNT(*) AS total_employees FROM employees GROUP BY department HAVING COUNT(*)
>2;
SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department HAVING SUM(salary)>120000;
SELECT leave_type, COUNT(*) AS total_requests FROM leave_requests GROUP BY leave_type;
SELECT leave_type, COUNT(*) AS total_requests FROM leave_requests GROUP BY leave_type HAVING COUNT(*)>3;
SELECT * FROM employees ORDER BY department ASC ,employee_name ASC;
SELECT department, AVG(salary) AS average_salary FROM employees GROUP BY department ORDER BY average_salary DESC LIMIT 1;
SELECT leave_type, SUM(leave_days) AS total_leave_days FROM leave_requests GROUP BY leave_type ORDER BY total_leave_days DESC LIMIT 1;
SELECT department, AVG(salary) AS average_salary FROM employees GROUP BY department HAVING AVG(salary)>55000;
SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department ORDER BY total_salary DESC LIMIT 2;
SELECT * FROM leave_requests WHERE leave_status = 'Approved' AND leave_days BETWEEN 2 AND 5;