
/*
                                    section =1
1)ows and columns
2)Record
3)One field of data
4)SELECT                                    
5)Unique for each row
6)Link tables
7)Missing/unknown value
8)UNIQUE
9. NOT NULL
10) Related data in structured form
11) Auto-increment ID
12) user_id in orders table
13) Structure of a database
14. CREATE TABLE
15. TEXT/VARCHAR
16. A comment field
17. Many columns
18. CHECK
19. Login and identity data
20. Data has clear relationships
                                section =B
                              Question =1(A)
Database: A place where all data is stored.
Table: Stores related data in rows and columns.
Row: One complete record.
Column: One piece (field) of information.
                                  Question = 1(b)
user_id	name	email
1	Rahul	rahul@gmail.com
2	Priya	priya@gmail.com

                                       (c)
During Signup, a new row is added to the users table.
During Login, the database checks the email and password from the users table.
                               Question = 2
                                  (A)
A Primary Key is a column that uniquely identifies each row in a table.
                                  (B)
user_id 	name
1	        Rahul
2	        Priya                                                                                                                                    
                                Question = 3
A Foreign Key is a column that connects one table to another.
                                    (B)
user_id	          name
1	              Rahul
2	              Priya

order_id	    user_id      	product
101	              1	            Laptop
102	              2          	Mouse  

Order 101 belongs to Rahul.
Order 102 belongs to Priya.

                                Question =4
NULL means the value is missing or unknown
                                  (B)
NOT NULL: Value is required.
UNIQUE: No duplicate values are allowed.
CHECK: Ensures a condition is true.

                                   (C)
NOT NULL: Every user must have an email.
UNIQUE: Every email address must be different.
CHECK: Age must be greater than 0 (age > 0).
                                  Question =5
Structured table design keeps data organized, accurate, and easy to manage. It also reduces duplicate data and makes the application faster and easier to maintain

                                   (B)
user_id    	name
1	        Rahul
2	        Priya

Orders Table

order_id	user_id   	product
101      	1	         Laptop
102	        1	         Mouse
103	        2	        Keyboard
                                    Section =C
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    created_at DATE
);

                                  Question =2
INSERT INTO users (user_id, name, email, phone, created_at)
VALUES
(1, 'Rahul', 'rahul@gmail.com', '9876543210', '2026-07-30'),
(2, 'Priya', 'priya@gmail.com', '9876543211', '2026-07-30'),
(3, 'Amit', 'amit@yahoo.com', '9876543212', '2026-07-30');
                                   question = 3
SELECT * FROM users;
                                 Question =  4
SELECT * FROM users
WHERE email LIKE '%@gmail.com';
                                Question =5
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15)
);
                                Question =6 
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    product_name VARCHAR(100),
    amount DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
                        Section =D
                         Question = 1.
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
                                                      
                               Question =2
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);                               

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
); */                                                                                                                                                                                       