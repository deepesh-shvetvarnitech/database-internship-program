/*                             SECTION = A
1) Entity-Relations
2) A real-world object or concept
3) Rectangle
4) How entities are connected
5) Diamond
6) Underlined attribute
7) One row in table A relates to one row in table B
8) One row in table A relates to many rows in table B
9) Many rows in table A relate to many rows in table B
10) The "many" side
11) A junction table
12) One-to-many
13) Many-to-many
14) Bridge table or linking table
15) Many orders
16) Many products
17) Child table
18) Referential integrity
19) User and user_profile
20) Visualizing database structure before implementation

                           SECTION = B
                         QUESTION = 1
ER (Entity-Relationship) Modeling is a way to plan and design a database before creating it.

important?
Prevents mistakes
Makes database easy to understand
Reduces duplicate data
Helps developers build backend correctly

Three Components of ER Diagram
Entity
Real-world object
Example:
User
Product
Order
Attribute
Information about an entity
Example
User
------
user_id
name
email
Relationship
Shows how entities are connected.

Example

User ---- Places ---- Order

                        QUESTION =2
One record in first table is connected to only one record in second table.

Example
users
user_id	                          name
1	                              Rahul
user_profile
profile_id	      user_id	          address
1	                1	                Delhi    
Rahul has only one profile.

Profile belongs to only Rahul.

Foreign Key
users
---------
user_id (PK)
name
user_profile
--------------
profile_id (PK)
user_id (FK)
address

SQL

CREATE TABLE users(
    user_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE user_profile(
    profile_id INT PRIMARY KEY,
    user_id INT UNIQUE,
    address VARCHAR(100),
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

UNIQUE ensures one profile per user.
  ALTER

                                  QUESTION =3
One row can connect to many rows.




Tables

users
user_id	           name
1	               Rahul
orders
order_id	      user_id
101             	1
102             	1
103	                1

Rahul placed three orders.

Foreign Key

Foreign key goes on the many side.

users
-------
user_id                       (PK)
orders
---------
order_id (PK)
user_id (FK)                                                      



                                 QUESTION =4
 Many rows in one table connect to many rows in another table.

Example

One order contains many products.

One product appears in many orders.

Orders  <-----> Products

Cannot store directly.

Need a junction table.

order_items
order_id	product_id
1	101
1	102
2	101
Why junction table?

Because SQL databases cannot directly store many-to-many relationships.

The junction table stores both foreign keY


                           QUESTION = 5
Relationship

User
 |
 | One
 |
Many
 |
Orders
 |
 | Many
 |
Order_Items
 |
Many
 |
Products
Relationship Types
Users → Orders
One-to-Many
Orders → Products
Many-to-Many

implemented using

order_items
                                Section C
                                QUESTION =1
 
 
CREATE TABLE users(
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
                                QUESTION = 2

CREATE TABLE products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);
                                 QUESTION = 3. 

CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    FOREIGN KEY(user_id)
    REFERENCES users(user_id)
);
                               QUESTION = 4

CREATE TABLE order_items(
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,

    FOREIGN KEY(order_id)
    REFERENCES orders(order_id),

    FOREIGN KEY(product_id)
    REFERENCES products(product_id)
);
                             QUESTION = 5

ALTER TABLE orders
ADD CONSTRAINT fk_user
FOREIGN KEY(user_id)
REFERENCES users(user_id);
                                 QUESTION = 6

SELECT
users.user_id,
users.name,
orders.order_id
FROM users
JOIN orders
ON users.user_id = orders.user_id;
                                 QUESTION = 7

SELECT
orders.order_id,
products.product_name,
order_items.quantity
FROM orders
JOIN order_items
ON orders.order_id = order_items.order_id
JOIN products
ON products.product_id = order_items.product_id;    

                               Section D
                               
                               QUESTION =1

Users
CREATE TABLE users(
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
Products
CREATE TABLE products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);
Orders
CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,

    FOREIGN KEY(user_id)
    REFERENCES users(user_id)
);
Order Items
CREATE TABLE order_items(
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,

    FOREIGN KEY(order_id)
    REFERENCES orders(order_id),

    FOREIGN KEY(product_id)
    REFERENCES products(product_id)
);
Relationships
users → orders = One-to-Many
orders → products = Many-to-Many (through order_items)
order_items acts as the junction (bridge) table.

                              QUESTION = 2

ER Diagram (Text)
                USERS
      +----------------------+
      | user_id (PK)         |
      | name                 |
      | email                |
      +----------------------+
               |
               | 1
               |
               | M
      +----------------------+
      | ORDERS              |
      | order_id (PK)       |
      | user_id (FK)        |
      | order_date          |
      +----------------------+
               |
               | 1
               |
               | M
      +----------------------+
      | ORDER_ITEMS         |
      | order_item_id (PK)  |
      | order_id (FK)       |
      | product_id (FK)     |
      | quantity            |
      +----------------------+
               |
               | M
               |
               | 1
      +----------------------+
      | PRODUCTS            |
      | product_id (PK)     |
      | product_name        |
      | price               |
      +----------------------+

Primary Keys
users.user_id
orders.order_id
products.product_id
order_items.order_item_id

Foreign Keys
orders.user_id → users.user_id
order_items.order_id → orders.order_id
order_items.product_id → products.product_id

Relationship Types

Users → Orders: One-to-Many (1:M)
Orders → Order_Items: One-to-Many (1:M)
Products → Order_Items: One-to-Many (1:M)
Orders ↔ Products: Many-to-Many (M:N), implemented using order_items

Why is this design suitable?
It avoids duplicate data (normalization).
It maintains data integrity using primary and foreign keys.
It scales well because one user can place many orders, and each order can contain multiple products without repeating product information.
