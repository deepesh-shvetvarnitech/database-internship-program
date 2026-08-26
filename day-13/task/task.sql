-- CREATE DATABASE company_management;
-- USE company_management;
-- CREATE TABLE departments(
--     department_id INT PRIMARY KEY,
--     department_name VARCHAR(100) NOT NULL UNIQUE
-- );
-- INSERT INTO departments (department_id,department_name)
-- VALUES
-- (1,'Engineering'),
-- (2,'HR'),
-- (3,'Finance'),
-- (4,'Marketing');
-- DROP TABLE employees CASCADE;
-- CREATE TABLE employees(
--     employee_id	       INT	          PRIMARY KEY,
--     employee_name	   VARCHAR(100)	  NOT NULL,
--     email	           VARCHAR(100)	  UNIQUE,
--     department_id	   INT	,
--     salary	           DECIMAL(10,2)	NOT NULL,
--     FOREIGN KEY( department_id) REFERENCES departments(department_id) 
-- );
-- INSERT INTO employees( employee_id,	employee_name,email	,department_id,salary)
-- VALUES
-- (101,'Rahu','Rahul@gmail.com',1,65000.00),
-- (102,'Priya','Priya@gmail.com',2,55000.00),
-- (103,'Aman','Aman@gmail.com',1,72000.00),
-- (104,'Neha','Neha@gmail.com',3,60000.00),
-- (105,'Rohan','Rohan@gmail.com',4,58000.00),
-- (106,'Sneha','Sneha@gmail.com',1,68000.00),
-- (107,'Vikas','Vikas@gmail.com',3,62000.00),
-- (108,'Anjali','Anajali@gmail.com',4,57000.00);
-- SELECT * FROM employees;


-- CREATE TABLE projects(
--     project_id        INT              PRIMARY KEY ,
--     project_name      VARCHAR(100)     NOT NULL ,
--     project_budget    DECIMAL(12,2)    NOT NULL
-- );
-- INSERT INTO projects (project_id,project_name,project_budget)
-- VALUES
-- (201,'AI Platform',500000.00),
-- (202,'Rag System',500000.00),
-- (203,'HR Managment System',500000.00),
-- (204,'Financial Dashboard',500000.00),
-- (205,'Marketing Website',500000.00);

-- CREATE TABLE employee_projects(
--     employee_id INT,
--     project_id INT,
--     PRIMARY KEY (employee_id,project_id),
--     FOREIGN KEY( employee_id) REFERENCES employees(employee_id),
--     FOREIGN KEY( project_id) REFERENCES projects(project_id)  
-- );
-- INSERT INTO employee_projects (employee_id,project_id)
-- VALUES
-- (101,201),
-- (101,202),
-- (103,201),
-- (106,201),
-- (102,203),
-- (104,204),
-- (107,204),
-- (105,205),
-- (108,205);

-- CREATE TABLE project_expenses(
--     expense_id	     INT	      PRIMARY KEY,
--     project_id	     INT	      ,
--     expense_type	 VARCHAR(50)	NOT NULL,
--     amount	         DECIMAL(10,2)	NOT NULL,
--     Foreign Key (project_id) REFERENCES projects (project_id) 
-- );

-- SELECT * FROM project_expenses;
-- INSERT INTO project_expenses(expense_id,project_id,expense_type,amount)
-- VALUES
-- (1,201,'Software',50000.00),
-- (2,201,'Hardware',75000.00),
-- (3,202,'Cloud',45000.00),
-- (4,202,'Software',30000.00),
-- (5,203,'Training',25000.00),
-- (6,203,'Hardware',40000.00),
-- (7,204,'Software',60000.00),
-- (8,204,'Cloud',35000.00),
-- (9,205,'Marketing',55000.00),
-- (10,205,'Advertising',70000.00);
-- SELECT employee_name,salary FROM employees;
-- SELECT project_name ,project_budget FROM projects;
-- SELECT employee_name ,salary FROM employees WHERE salary BETWEEN 50000 AND 80000;
-- SELECT employee_name, department_id FROM employees WHERE deparment_id IN(1,3);

-- SELECT employee_name FROM employees WHERE employee_name LIKE 'A%';

-- SELECT employee_name ,salary FROM employees ORDER BY salary DESC LIMIT 3;
-- SELECT project_name , project_budget FROM projects ORDER BY project_budget DESC LIMIT 1;
-- SELECT project_name , project_budget FROM projects ORDER BY project_budget ;
-- SELECT  expense_id,project_id ,expense_type ,amount FROM  project_expenses ORDER BY  amount DESC LIMIT 2;
-- SELECT DISTINCT expense_type FROM project_expenses;
-- SELECT COUNT(*) AS total_employees FROM employees;
-- SELECT AVG(salary) AS average_salary from employees;
SELECT MAX(salary) AS highest_salary from employees;
SELECT MIN(salary) AS lowest_salary from employees;
SELECT SUM(project_budget) AS total_project_expenses from projects;
SELECT
(SELECT COUNT(*)  FROM employees )AS total_employees,
 (SELECT AVG(salary) AS average_salary From employees) AS average_salary,
 (SELECT MAX(salary) From employees) AS highest_salary ,
 (SELECT MIN(salary) From employees) AS lowest_salary,
 (SELECT SUM(project_budget) From projects) AS total_project_expenses ,
 (SELECT SUM(amount) FROM project_expenses) AS total_project_expaenses;
SELECT d.department_name AS department,
COUNT(e.employee_id) AS employee_count
FROM departments d LEFT JOIN employees e ON d.department_id = e.department_id GROUP BY d.department_id ,d.department_name;
SELECT d.department_name AS department,
AVG(e.salary) AS average_salary
FROM departments d  JOIN employees e ON d.department_id = e.department_id GROUP BY d.department_id ,d.department_name;

SELECT p.project_name AS project,
SUM(pe.amount) AS total_expenses
FROM projects p JOIN project_expenses  pe ON p.project_id = pe.project_id GROUP BY p.project_id ,p.project_name;
SELECT d.department_name AS department,
COUNT(e.employee_id) AS employee_count
FROM departments d  JOIN employees e ON d.department_id = e.department_id GROUP BY d.department_id ,d.department_name HAVING COUNT(e.employee_id)>1;
SELECT p.project_name AS project,
SUM(pe.amount) AS total_expenses
FROM projects p JOIN project_expenses  pe ON p.project_id = pe.project_id GROUP BY p.project_id ,p.project_name HAVING SUM(pe.amount)>50000;
SELECT e.employee_name, d.department_name,e.salary FROM employees e INNER JOIN departments d ON e.department_id = d.department_id;

SELECT e.employee_name, d.department_name AS department, p.project_name FROM employees e INNER JOIN departments d ON e.department_id = d.department_id INNER JOIN employee_projects ep ON e.employee_id = ep.employee_id INNER JOIN projects p ON ep.project_id  = p.project_id;
SELECT e.employee_name ,p.project_name FROM employees e LEFT JOIN employee_projects ep ON e.employee_id = ep.employee_id LEFT JOIN projects  p  ON ep.project = p.project_id;

SELECT AVG(salary) FROM employees;

SELECT employee_name salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees );
SELECT employee_name , department_id FROM  employees  WHERE department_id  = (SELECT department_id FROM employees WHERE employee_name = 'Rahul');
SELECT p.project_name 
SUM(pe.amount) AS total_expenses
FROM projects p JOIN project_expenses  pe ON p.project_id = pe.project_id GROUP BY p.project_id ,p.project_name HAVING SUM(pe.amount)>(SELECT AVG (project_total)FROM ( SELECT SUM (amount) AS project_total FROM project_expenses GROUP BY project_id  ) AS project_expenses_summmary);
SELECT e.employee_name ,e.salary ,p.project_name FROM employees e INNER JOIN employee_projects ep  ON  e.employee_id = ep.employee_id INNER JOIN projects p ON ep.project_id = p.project_id WHERE e.salary > (SELECT AVG(salary) FROM employees) ORDER BY e.salary DESC; 
/*
1
FIRST NORMAL FUNCTION
table m harcolumn m single atomic value hone chaiye .
ek cell m multiple values nhi hone chahiye

2
2nf ka malab ha  1 nf hp or koi non key column
composite primary key k sirf composite part pr depend na kare GROUP BY
yani partitial denendencies nhi one chahiye
3
3nf ka matlab hai 2nf m ho or non key non key column pr depend na kare 

4
employee or projects b bich m many to many to many relation ship HA
ek employee multiple project pr kaam kar sakta hai

5
 employee<_> project = many tomnay relationship hai
6
Q KI EMPLOYEE MULTIPLE PROJECT PR KAAM KAR RHE HAI
7
DEPARTMENT K NAAM PR BAR BAR STORE KARNE SE DATA DUPLICATE HOTA HAI 
 8
  employee projects
  
  */
SELECT d.department_name AS department,
AVG(e.salary) AS average_salary
FROM departments d  JOIN employees e ON d.department_id = e.department_id GROUP BY d.department_id ,d.department_name ORDER BY average_salary DESC LIMIT 1;







