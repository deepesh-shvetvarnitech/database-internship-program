-- CREATE TABLE employees(
--     employee_id	         INT	        PRIMARY KEY,
--     employee_name	     VARCHAR(100)	NOT NULL,
--     email	             VARCHAR(100)	UNIQUE,
--     department	         VARCHAR(50)	NOT NULL,
--     salary	             DECIMAL(10,2)	NOT NULL
-- );
-- CREATE TABLE performance(
--     performance_id	     INT	       PRIMARY KEY,
--     employee_id	         INT	       NOT NULL,
--     performance_score	 INT	       NOT NULL,
--     rating	             VARCHAR(20)	NOT NULL,
--     Foreign Key (employee_id) REFERENCES employees (employee_id)
-- );
-- INSERT INTO employees ( employee_id	, employee_name ,email ,department ,salary)
-- VALUES
-- (1,	'Rahul',	        'Rahul@gmail.com','Engineering',   	60000),
-- (2, 'Priya', 'Priya@gmail.com','HR',45000),
-- (3,	'Aman',	           'Aman@gmail.com',	'Engineering',      75000),
-- (4,	'Neha',	            'Neha@gmail.com','Finance',    	55000),
-- (5,	'Rohan',	       'Rohan@gmail.com','Marketing',  	50000),
-- (6,	'Anjali',	       'Anajali@gmail.com','Engineering',  	65000),
-- (7,	'Karan'	,             'Karan@gmail.com','Finance', 	58000),
-- (8,	'Sneha',	               'Sneha@gmail.com','HR',  	47000);
-- SELECT * FROM employees;
-- INSERT INTO performance( performance_id, employee_id,performance_score, rating)
-- VALUES
-- (101,	1,	82,	'Good'),
-- (102,	2,	75,	'Good'),
-- (103,	3,	92	,'Excellent'),
-- (104,	4,	78,	'Good'),
-- (105,	5,	69,	'Average'),
-- (106,	6,	88,	'Excellent'),
-- (107,	7,	81,	'Good'),
-- (108,	8,	73	,'Average');
-- SELECT * FROM performance;
-- SELECT * FROM employees WHERE salary > (
--     SELECT AVG(salary)
--     FROM employees
-- );
SELECT * FROM employees WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);
SELECT * FROM employees WHERE salary > (
    SELECT salary
    FROM employees
    WHERE employee_name = 'Rahul'
);
SELECT * FROM employees WHERE department = (
    SELECT department
    FROM employees
    WHERE employee_name = 'Rahul'
);
SELECT employee_id,performance_score,rating FROM performance WHERE performance_score > (
    SELECT AVG(performance_score)
    FROM performance
);
SELECT employee_id,performance_score,rating FROM performance WHERE performance_score >= (
    SELECT MAX(performance_score) - 5
    FROM performance
);
SELECT * FROM employees WHERE department IN (
    SELECT department
    FROM employees
    WHERE salary > 70000
);
SELECT  employee_name,department,salary 
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department = e.department
);
SELECT e.employee_name,
e.department,
p.performance_score,
p.rating 
FROM employees e JOIN performance p ON e.employee_id = p.employee_id WHERE p.performance_score >(SELECT  AVG(performance_score) FROM performance);

SELECT e.employee_name,
e.department,
p.performance_score,
p.rating 
FROM employees e JOIN performance p ON e.employee_id = p.employee_id WHERE p.performance_score =(SELECT  MAX(performance_score) FROM performance);
SELECT COUNT(*)
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > (
    SELECT AVG(salary)
    FROM employees
);
SELECT e.employee_name,
e.department,
p.performance_score,
p.rating 
FROM employees e JOIN performance p ON e.employee_id = p.employee_id WHERE e.salary>(SELECT  AVG(salary) FROM employees) AND  p.performance_score > (SELECT AVG(performance_score)FROM performance) ORDER BY e,salary DESC;
SELECT  employee_name,salary FROM employees WHERE salary = (SELECT MIN(salary) FROM employees);
SELECT  employee_name,salary FROM employees WHERE salary BETWEEN(SELECT AVG(salary) FROM employees)AND(SELECT MAX(salary) FROM employees);
SELECT employee_id,performance_score,rating FROM performance WHERE performance_score = (SELECT AVG(performance_score) FROM performance);
SELECT  employee_name,salary FROM employees WHERE salary = (SELECT MAX(salary) FROM employees WHERE salary<(SELECT MAX(salary) FROM employees));
SELECT * FROM employees WHERE department IN (SELECT department FROM employees WHERE salary > 60000 );