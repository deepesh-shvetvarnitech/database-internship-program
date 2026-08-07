


-- CREATE TABLE members (
--     member_id INT PRIMARY KEY,
--     member_name VARCHAR(100) NOT NULL,
--     email VARCHAR(100) UNIQUE,
--     phone VARCHAR(15) NOT NULL
-- );

-- SELECT * FROM members;
-- CREATE TABLE membership_cards (
--     card_id INT PRIMARY KEY,
--     member_id INT UNIQUE,
--     issue_date DATE NOT NULL,
--     expiry_date DATE NOT NULL,

--     FOREIGN KEY (member_id)
--     REFERENCES members(member_id)
-- );
-- SELECT * FROM membership_cards;
-- CREATE TABLE books (
-- book_id INT PRIMARY KEY,
-- book_title VARCHAR(100) NOT NULL,
--     author VARCHAR(100) NOT NULL,
--     category VARCHAR(50) NOT NULL
-- );
-- CREATE TABLE borrow_records (
--     borrow_id INT PRIMARY KEY,
--     member_id INT,
--     book_id INT,
--     borrow_date DATE NOT NULL,

--     FOREIGN KEY (member_id)
--     REFERENCES members(member_id),

--     FOREIGN KEY (book_id)
--     REFERENCES books(book_id)
-- );

-- INSERT INTO members (member_id,member_name,email,phone)
-- VALUES
-- (1, 'Rahul', 'rahul@gmail.com', '9876543210'),
-- (2, 'Priya', 'priya@gmail.com', '9876543211'),
-- (3, 'Aman', 'aman@gmail.com', '9876543212');
-- SELECT * FROM members;


-- INSERT INTO membership_cards(card_id,member_id,issue_date,expiry_date)
-- VALUES
-- (1001, 1, '2026-01-01', '2027-01-01'),
-- (1002, 2, '2026-01-02', '2027-01-02'),
-- (1003, 3, '2026-01-13', '2027-01-13');
-- SELECT * FROM membership_cards;


-- INSERT INTO books(book_id,book_title,author,category)
-- VALUES
-- (101, 'Python Programming', 'John Smith', 'Programming'),
-- (102, 'SQL Basics', 'David Miller', 'Database'),
-- (103, 'Data Structures', 'Robert Brown', 'Computer Science');

-- SELECT * FROM books;
-- INSERT INTO borrow_records(borrow_id, member_id, book_id, borrow_date)
-- VALUES
-- (1, 1, 101, '2026-07-01'),
-- (2, 1, 102, '2026-07-03'),
-- (3, 2, 102, '2026-07-05'),
-- (4, 3, 103, '2026-07-07');
-- SELECT * FROM borrow_records ;


-- -- members → membership_cards = One-to-One

-- -- members → borrow_records = One-to-Many

-- -- books → borrow_records = One-to-Many

-- -- members ↔ books = Many-to-Many





-- -- Answer:
-- -- members


-- -- Answer:
-- -- books


-- -- Answer:
-- -- borrow_records acts as a bridge (junction) table.


-- -- Answer:
-- -- members ↔ membership_cards


-- -- Answer:
-- -- members ↔ books
-- INSERT INTO books(book_id,book_title,author,category)
-- VALUES
-- (104, 'Machine Learning', 'Andrew Ng', 'Artificial Intelligence');

SELECT * FROM books;

