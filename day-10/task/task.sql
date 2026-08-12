DROP TABLE employees CASCADE;
CREATE TABLE employees(
   employee_id INT PRIMARY key,
   employee_name VARCHAR(50),
   department VARCHAR(50)
);
CREATE TABLE projects(
   project_id INT PRIMARY key,
   project_name VARCHAR(100),
   manager_name VARCHAR(50),
   manager_email VARCHAR(100)

);
CREATE TABLE employee_projects(
    employee_id INT,
    project_id int,
    PRIMARY KEY (employee_id,project_id),
    Foreign Key (employee_id) REFERENCES employees (employee_id),
    Foreign Key (project_id) REFERENCES projects (project_id)
);
INSERT INTO employees
(employee_id,employee_name,department)
VALUES
(1,'Rahul','Engineering'),
(2,'Priya','HR'),
(3,'Aman','Engineering'),
(4,'Neha','Finance'),
(5,'Rohan','Marketing');
SELECT * FROM employees;

INSERT INTO projects(project_id,project_name,manager_name,manager_email)
VALUES
(101,	'AI Platform',	    'Amit',	'amit@shvetvarni.com'),
(102,	'RAG System',	   'Neha',	'neha@shvetvarni.com'),
(103,	'HR Portal',	       'Karan',	'karan@shvetvarni.com'),

(104,	'Finance App',	   'Priya',	'priya@shvetvarni.com'),
(105, 	'Marketing Portal','Karan',	'karan@shvetvarni.com');
INSERT INTO employee_projects(employee_id,project_id)
VALUES
(1,101),
(1,102),
(2,103),
(3,101),
(4,104),
(5,105);

CREATE TABLE managers(
    manager_id INT PRIMARY KEY,
    manager_name VARCHAR(50) NOT NULL ,
   manager_email VARCHAR(100) NOT NULL UNIQUE

);
INSERT INTO managers(manager_id, manager_name,manager_email)
VALUES
(1,	'Amit',	'amit@shvetvarni.com'),
(2,	'Neha',	'neha@shvetvarni.com'),
(3,	'Karan',	'karan@shvetvarni.com'),
(4,	'Priya',	'priya@shvetvarni.com');
CREATE TABLE employees(
   employee_id INT PRIMARY key,
   employee_name VARCHAR(50) NOT NULL,
   department VARCHAR(50) NOT NULL
);


CREATE TABLE employees(
   employee_id INT PRIMARY key,
   employee_name VARCHAR(50) NOT NULL,
   department VARCHAR(50) NOT NULL
);
CREATE TABLE managers(
    manager_id INT PRIMARY KEY,
    manager_name VARCHAR(50) NOT NULL ,
   manager_email VARCHAR(100) NOT NULL UNIQUE

);
CREATE TABLE projects(
   project_id INT PRIMARY key,
   project_name VARCHAR(100) NOT NULL,
   manager_id INT NOT NULL,
   Foreign Key (manager_id) REFERENCES managers (manager_id)
);
CREATE TABLE employee_projects(
    employee_id INT NOT NULL,
    project_id int NOT NULL,
    PRIMARY KEY (employee_id,project_id),
    Foreign Key (employee_id) REFERENCES employees (employee_id),
    Foreign Key (project_id) REFERENCES projects (project_id)
);
SELECT e.employee_name AS Employee,
p.project_name AS Project,
m.manager_name AS Manager
FROM employees e
JOIN employee_projects ep
ON e.employee_id = ep.employee_id
JOIN projects p ON ep.project_id = p.project_id
JOIN managers m ON p.manager_id = m.manager_id;
/*
1 NF
MEANS FIRST NORMAL FORM 
EACH COLUMN  MUST CONTAIN SINGLE VALUES
THERE SHOULD BE NO REPEATING GROUPS
EACH RAW REPRESENTS ONE RECORD
2 NF
MEANS  SECOND  NORMAL FORM 
IT REMOVES PARTIAL DEPENDENCIES
NON KEY COLUMN SHOULD DEPEND ON THE WHOLE PRIMARY KEY

3 NF
MEANS  THIREDD  NORMAL FORM 
IT REMOVES TRANSPERENCY DEPENDENCIES

WHY WAS THE MANAGER TABLE CREATE
THE MANAGERS TABLE STORE MANAGER INFORMATION
WHY WAS THE EMPLOYEE_PROJECT TABLE CREATE
THE EMPLOYEE_PROJECT TABLE STORE EMPLOYEE_PROJECT INFORMATION

WHAT RELATIONSHIP EXIST BETWEEN EMPLOYEE AND PROJECTS
THEY HAVE MANY TO MANY 
ONE EMPLOYEE CAN WORK MANY PROECT
*/
/*
TASK 2
1
EMPLOYEE INFORMATION ,PROJECT INFORMATION AND MANAGER INFORMATIN
2
EMPLOYEE_ID,EMPLOYEE_NAME AND DEPARTMENT
3
PROJECT_ID AND PROJECT_NAME
4
MANAGER_NAME AND MANAGER_EMAIL
5
BECAUSE SAME INFO IS STORED IN MANY RECORD

TASK 3
1NF 
THER ARE NO MLTIPLE VALUES CONTAINS SINGLE VALUE
EXAMPLE
*/
SELECT p.project_name FROM employees e JOIN employee_projects ep ON e.employee_id = ep.employee_id JOIN projects p ON ep.project_id WHERE e.employee_name ='Rahul';
SELECT e.employee_name FROM employees e  JOIN employee_projects ep ON e.employee_id  = ep.employee_id JOIN projects p ON ep.project_id =p.project_id WHERE p.project_name ='AI Platform';
SELECT p.project_name FROM projects p JOIN managers m ON p.manager_id = m.manager_id WHERE m.manager_name = 'Karan';

SELECT p.project_name,COUNT (ep.employee_id) AS employee_count FROM projects  p LEFT JOIN employee ep ON p.project_id = ep.project_id GROUP BY p.project_id,p.project_name;
SELECT p.project_name,COUNT (ep.employee_id) AS employee_count FROM projects p JOIN employee_projects ep ON p.project_id = ep.project_id GROUP BY p.project_id,p.project_name HAVING COUNT(ep.employee_id)
>1;





