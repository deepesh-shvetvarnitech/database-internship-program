'''
1 SQL injection
2 — User input directly concatenated into SQL queries
3 — Parameterized queries
4 — ?
5 — SQL and data are sent separately
6 — f-string query
7 — All of the above
8 — All of the above
9 — User input is treated as data, not executable code
10 — Parameterized query using ?
11— Checking input type, length, and format
12— Single quote (')
13— ' OR '1'='1
14— Neutralize potentially dangerous characters
15— Always use parameterized queries
16— Users have only necessary permissions
17— Direct string concatenation in queries
18— Parameterized queries
19— Hide detailed errors from users
20— Parameterized queries + input validation + least privilege
'''
#                                        SECTION = B
'''                                       
                                         QUESTION = 1
SQL injection is an attack where an attacker puts malicious SQL code into user input. If the application directly joins that input with an SQL query, the attacker may change the query's meaning.

Unsafe:

query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)

An attacker may enter special SQL input that changes the WHERE condition and potentially bypass authentication or access unauthorized data.

                                               QUESTION = 2
Parameterized queries keep SQL commands and user input separate. User input is treated as data, not SQL code.

Unsafe:

query = f"SELECT * FROM users WHERE name = '{name}'"
cursor.execute(query)

Safe:

query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (name,))

The ? is a placeholder, and the value is supplied separately.

                                                 QUESTION = 3
Input validation checks whether user input is acceptable before using it in an application. It provides an additional security layer even when parameterized queries are used.

Three examples:

Check data type — ID should be an integer.
Check length — username should not be excessively long.
Check format — email should follow a valid email format.

                                                 QUESTION = 4
Defense in depth means using multiple security layers instead of depending on only one security method.

Three layers are:

Parameterized queries — prevent user input from becoming SQL code.
Input validation — check type, length, and format.
Least privilege — give the database user only the permissions it actually needs.


                                        SECTION = C
                                       QUESTION = 1

Vulnerable: Yes
Reason: f-string directly adds user input into SQL.

query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
                                       QUESTION =  2

Vulnerable: No
Reason: It uses a parameterized query with ?.

query = "SELECT * FROM products WHERE category = ?"
cursor.execute(query, (category,))
                                      QUESTION = 3

Vulnerable: Yes
Reason: User input is directly concatenated into the SQL query.

query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user
                                           QUESTION = 4

Vulnerable: Yes
Reason: % string formatting directly inserts values into SQL.

query = "UPDATE users SET email = ? WHERE id = ?"
cursor.execute(query, (new_email, user_id))
connection.commit()                                        

                                                 SECTION = D
                                                question = 1:
import sqlite3


connection = sqlite3.connect("day16.db")
cursor = connection.cursor()




def secure_login(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        return None


    if len(username) < 3 or len(username) > 50:
        return None


    if len(password) < 6 or len(password) > 100:
        return None


    query = """
        SELECT * FROM users
        WHERE username = ? AND password = ?
    """


    try:
        cursor.execute(query, (username, password))
        return cursor.fetchone()
    except sqlite3.Error:
        return None
                                               question = 2
def secure_search_products(search_term):
    if not isinstance(search_term, str):
        return []


    search_term = search_term.strip()


    if len(search_term) == 0 or len(search_term) > 50:
        return []


    for char in search_term:
        if not (char.isalnum() or char in " -_"):
            return []


    search_pattern = "%" + search_term + "%"


    query = """
        SELECT * FROM products
        WHERE name LIKE ?
    """


    try:
        cursor.execute(query, (search_pattern,))
        return cursor.fetchall()
    except sqlite3.Error:
        return
                                           Question = 3
import re




def secure_register_user(username, email, password):
    if not isinstance(username, str):
        return False


    if not isinstance(email, str):
        return False


    if not isinstance(password, str):
        return False


    username = username.strip()
    email = email.strip()


    if len(username) < 3 or len(username) > 50:
        return False


    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"


    if not re.match(email_pattern, email):
        return False


    if len(password) < 8:
        return False


    if not re.search(r"[A-Z]", password):
        return False


    if not re.search(r"[a-z]", password):
        return False


    if not re.search(r"[0-9]", password):
        return False


    query = "SELECT id FROM users WHERE email = ?"


    try:
        cursor.execute(query, (email,))


        if cursor.fetchone():
            return False


        query = """
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
        """


        cursor.execute(query, (username, email, password))
        connection.commit()


        return True


    except sqlite3.Error:
        connection.rollback()
        return False
                                       question = 4
def create_user(name, email, age):




def update_user(user_id, name, email):
    """Update a user's name and email."""


    if not isinstance(user_id, int) or user_id <= 0:
        return False


    if not isinstance(name, str) or not name.strip():
        return False


    if not isinstance(email, str) or "@" not in email:
        return False


    query = """
        UPDATE users
        SET name = ?, email = ?
        WHERE id = ?
    """


    try:
        cursor.execute(query, (name.strip(), email.strip(), user_id))
        connection.commit()


        return cursor.rowcount > 0


    except sqlite3.Error:
        connection.rollback()
        return False




def delete_user(user_id):
    """Delete a user by ID."""


    if not isinstance(user_id, int) or user_id <= 0:
        return False


    query = """
        DELETE FROM users
        WHERE id = ?
    """


    try:
        cursor.execute(query, (user_id,))
        connection.commit()


        return cursor.rowcount > 0


    except sqlite3.Error:
        connection.rollback()
        return False




def list_users_by_city(city):
    """Return all users from a specific city."""


    if not isinstance(city, str) or not city.strip():
        return []


    query = """
        SELECT * FROM users
        WHERE city = ?
    """


    try:
        cursor.execute(query, (city.strip(),))
        return cursor.fetchall()


    except sqlite3.Error:
        return []       '''                                          