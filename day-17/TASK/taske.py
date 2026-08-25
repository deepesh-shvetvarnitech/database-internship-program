'''                                                    SECTION = A
                                                      QUESTION = 1

                                                      
SQL Injection ek security problem hai jisme user galat ya malicious input dekar SQL query ka meaning change karne ki koshish karta hai.

                                                       QUESTION =2


Ye unsafe hai kyunki user ka email directly SQL query ke andar add ho raha hai.

Agar user malicious SQL input deta hai, to wo query ka meaning change kar sakta hai aur unwanted customer records mil sakte hain.
       

                                                  QUESTION =3
Ye safer hai kyunki ? ek placeholder hai.

User ka input SQL code nahi banta, balki ek normal value ke roop me treat hota hai.



                                              QUESTION =4
    User-provided values ko directly SQL query me concatenate nahi karna chahiye kyunki attacker malicious input de sakta hai.

Isse SQL Injection ho sakta hai aur attacker unwanted data access ya modify karne ki koshish kar sakta hai.






                                                 QUESTION = 5
cursor.execute(
    """
    INSERT INTO customers (name, email, city)
    VALUES (?, ?, ?)
    """,
    (name, email, city)
)

Ye method safer hai kyunki values ? placeholders ke through pass hoti hain.

Isme user input SQL query ka part nahi banta, isliye SQL Injection ka risk kam hota hai.



















'''

































import sqlite3

connection = None

try:
    connection = sqlite3.connect("ecommerce.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            city TEXT NOT NULL,
            balance INTEGER NOT NULL
        )
    """)

    print("Database and table created successfully")

    customers = [
        ("Rahul Sharma", "rahul@example.com", "Delhi", 5000),
        ("Priya Singh", "priya@example.com", "Mumbai", 7500),
        ("Amit Verma", "amit@example.com", "Pune", 3000)
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO customers
        (name, email, city, balance)
        VALUES (?, ?, ?, ?)
    """, customers)

    connection.commit()

    print("Customers inserted successfully")

    def search_customer(email):
        cursor.execute(
            "SELECT * FROM customers WHERE email = ?",
            (email,)
        )
        return cursor.fetchone()

    def update_customer(email, new_city):
        cursor.execute(
            """
            UPDATE customers
            SET city = ?
            WHERE email = ?
            """,
            (new_city, email)
        )
        connection.commit()

    def get_customers_by_balance(min_balance):
        cursor.execute(
            """
            SELECT name, email, balance
            FROM customers
            WHERE balance > ?
            """,
            (min_balance,)
        )
        return cursor.fetchall()

    email = input("Enter customer email: ")

    customer = search_customer(email)

    if customer:
        print("Customer Found")
        print("ID:", customer[0])
        print("Name:", customer[1])
        print("Email:", customer[2])
        print("City:", customer[3])
        print("Balance:", customer[4])
    else:
        print("Customer not found")

    email = input("Enter customer email to update city: ")
    new_city = input("Enter new city: ")

    update_customer(email, new_city)

    customer = search_customer(email)

    if customer:
        print("Customer updated successfully")
        print("ID:", customer[0])
        print("Name:", customer[1])
        print("Email:", customer[2])
        print("City:", customer[3])
        print("Balance:", customer[4])
    else:
        print("Customer not found")

    min_balance = int(input("Enter minimum balance: "))

    customers = get_customers_by_balance(min_balance)

    for customer in customers:
        print(customer[0], "-", customer[1], "-", customer[2])

    test_email = "' OR '1'='1"

    customer = search_customer(test_email)

    if customer:
        print("Customer Found")
    else:
        print("Customer not found")

except sqlite3.Error as error:
    print("Database error:", error)

except ValueError:
    print("Please enter a valid balance")

finally:
    if connection:
        connection.close()

    print("Database connection closed")