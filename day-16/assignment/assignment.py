

#                                   QUESTION =1




# import sqlite3




# def display_all_books(cursor):
#     cursor.execute("SELECT * FROM books")

#     books = cursor.fetchall()

#     print("\n--- All Books ---")

#     for book in books:
#         print(
#             f"ID: {book[0]} | "
#             f"Title: {book[1]} | "
#             f"Author: {book[2]} | "
#             f"Category: {book[3]} | "
#             f"Price: {book[4]}"
#         )

#     print(f"Total Books: {len(books)}")



# def get_expensive_books(cursor):
#     cursor.execute(
#         "SELECT * FROM books WHERE price > ?",
#         (500,)
#     )

#     books = cursor.fetchall()

#     print("\n--- Expensive Books ---")

#     for book in books:
#         print(f"{book[1]} - {book[4]}")




# connection = None

# try:


#     connection = sqlite3.connect("library.db")

#     cursor = connection.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS books (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT NOT NULL,
#             author TEXT NOT NULL,
#             category TEXT NOT NULL,
#             price INTEGER NOT NULL
#         )
#     """)

#     connection.commit()

#     print("Database and table created successfully")

#     books = [
#         ("Python Basics", "James Smith", "Programming", 450),
#         ("Database Fundamentals", "Robert Brown", "Database", 550),
#         ("Web Development", "John Miller", "Web", 400)
#     ]

#     cursor.executemany("""
#         INSERT INTO books
#         (title, author, category, price)
#         VALUES (?, ?, ?, ?)
#     """, books)

#     connection.commit()

#     print("Books inserted successfully")



#     display_all_books(cursor)


#     book_title = input("\nEnter book title: ")

#     cursor.execute(
#         "SELECT * FROM books WHERE title = ?",
#         (book_title,)
#     )

#     book = cursor.fetchone()

#     if book:
#         print("\nBook Found")

#         print(f"ID: {book[0]}")
#         print(f"Title: {book[1]}")
#         print(f"Author: {book[2]}")
#         print(f"Category: {book[3]}")
#         print(f"Price: {book[4]}")

#     else:
#         print("Book not found")



#     cursor.execute(
#         "SELECT id FROM books WHERE title = ?",
#         ("Python Basics",)
#     )

#     python_book = cursor.fetchone()

#     if python_book:

#         book_id = python_book[0]

#         cursor.execute(
#             "UPDATE books SET price = ? WHERE id = ?",
#             (500, book_id)
#         )

#         connection.commit()

#         print("\nPrice updated successfully")

       

#         cursor.execute(
#             "SELECT * FROM books WHERE id = ?",
#             (book_id,)
#         )

#         updated_book = cursor.fetchone()

#         print(
#             f"ID: {updated_book[0]} | "
#             f"Title: {updated_book[1]} | "
#             f"Author: {updated_book[2]} | "
#             f"Category: {updated_book[3]} | "
#             f"Price: {updated_book[4]}"
#         )


    

#     cursor.execute(
#         "DELETE FROM books WHERE title = ?",
#         ("Web Development",)
#     )

#     connection.commit()

#     print("\nWeb Development deleted successfully")

#     print("\n--- Remaining Books ---")

#     cursor.execute("SELECT * FROM books")

#     remaining_books = cursor.fetchall()

#     for book in remaining_books:
#         print(
#             f"ID: {book[0]} | "
#             f"Title: {book[1]} | "
#             f"Author: {book[2]} | "
#             f"Category: {book[3]} | "
#             f"Price: {book[4]}"
#         )


  

#     category = input("\nEnter category to search: ")

#     cursor.execute(
#         "SELECT * FROM books WHERE category = ?",
#         (category,)
#     )

#     category_books = cursor.fetchall()

#     if category_books:
#         print("\nBooks in this category:")

#         for book in category_books:
#             print(
#                 f"{book[1]} - "
#                 f"{book[2]} - "
#                 f"{book[4]}"
#             )
#     else:
#         print("No books found in this category")


    

#     get_expensive_books(cursor)


# except sqlite3.Error as error:

#     print(f"Database error: {error}")


# finally:

#     if connection:
#         connection.close()

#         print("\nDatabase connection closed")



#                                     QUESTION =2





# import sqlite3



# def display_all_students(cursor):

#     cursor.execute("SELECT * FROM students")

#     students = cursor.fetchall()

#     print("\n--- All Students ---")

#     for student in students:
#         print(
#             f"ID: {student[0]} | "
#             f"Name: {student[1]} | "
#             f"Course: {student[3]} | "
#             f"Marks: {student[4]}"
#         )

#     print(f"Total Students: {len(students)}")




# def get_top_students(cursor):

#     cursor.execute(
#         "SELECT * FROM students WHERE marks > ?",
#         (80,)
#     )

#     students = cursor.fetchall()

#     print("\n--- Top Students ---")

#     for student in students:
#         print(f"{student[1]} - {student[4]}")



# connection = None

# try:

    
#     connection = sqlite3.connect("school.db")

#     cursor = connection.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS students (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             course TEXT NOT NULL,
#             marks INTEGER NOT NULL
#         )
#     """)

#     connection.commit()

#     print("Database and table created successfully")


    
#     students = [
#         ("Arjun Patel", "arjun@example.com", "Python", 78),
#         ("Neha Sharma", "neha@example.com", "Java", 85),
#         ("Rohit Singh", "rohit@example.com", "Python", 67)
#     ]

#     cursor.executemany("""
#         INSERT INTO students
#         (name, email, course, marks)
#         VALUES (?, ?, ?, ?)
#     """, students)

#     connection.commit()

#     print("Students inserted successfully")


   
#     display_all_students(cursor)


    

#     student_name = input("\nEnter student name: ")

#     cursor.execute(
#         "SELECT * FROM students WHERE name = ?",
#         (student_name,)
#     )

#     student = cursor.fetchone()

#     if student:

#         print("\nStudent Found")

#         print(f"ID: {student[0]}")
#         print(f"Name: {student[1]}")
#         print(f"Email: {student[2]}")
#         print(f"Course: {student[3]}")
#         print(f"Marks: {student[4]}")

#     else:

#         print("Student not found")


    

#     cursor.execute(
#         "SELECT id FROM students WHERE name = ?",
#         ("Arjun Patel",)
#     )

#     arjun = cursor.fetchone()

#     if arjun:

#         arjun_id = arjun[0]

#         cursor.execute(
#             "UPDATE students SET marks = ? WHERE id = ?",
#             (90, arjun_id)
#         )

#         connection.commit()

#         print("\nMarks updated successfully")

        

#         cursor.execute(
#             "SELECT * FROM students WHERE id = ?",
#             (arjun_id,)
#         )

#         updated_student = cursor.fetchone()

#         print(
#             f"ID: {updated_student[0]} | "
#             f"Name: {updated_student[1]} | "
#             f"Course: {updated_student[3]} | "
#             f"Marks: {updated_student[4]}"
#         )


    

#     cursor.execute(
#         "DELETE FROM students WHERE name = ?",
#         ("Rohit Singh",)
#     )

#     connection.commit()

#     print("\nRohit Singh deleted successfully")


#     # Display remaining students

#     print("\n--- Remaining Students ---")

#     cursor.execute("SELECT * FROM students")

#     remaining_students = cursor.fetchall()

#     for student in remaining_students:

#         print(
#             f"ID: {student[0]} | "
#             f"Name: {student[1]} | "
#             f"Course: {student[3]} | "
#             f"Marks: {student[4]}"
#         )


    
#     get_top_students(cursor)


# except sqlite3.Error as error:

#     print(f"Database error: {error}")


# finally:

#     if connection:

#         connection.close()

#         print("\nDatabase connection closed")



#                            QUESTION =3



# 

# import sqlite3



# def display_all_patients(cursor):

#     cursor.execute("SELECT * FROM patients")

#     patients = cursor.fetchall()

#     print("\n--- All Patients ---")

#     for patient in patients:
#         print(
#             f"ID: {patient[0]} | "
#             f"Name: {patient[1]} | "
#             f"Disease: {patient[3]} | "
#             f"Bill: {patient[4]}"
#         )

#     print(f"Total Patients: {len(patients)}")



# def get_high_bill_patients(cursor):

#     cursor.execute(
#         "SELECT * FROM patients WHERE bill > ?",
#         (4000,)
#     )

#     patients = cursor.fetchall()

#     print("\n--- High Bill Patients ---")

#     for patient in patients:
#         print(f"{patient[1]} - {patient[4]}")




# connection = None

# try:

    

#     connection = sqlite3.connect("hospital.db")

#     cursor = connection.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS patients (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             phone TEXT UNIQUE NOT NULL,
#             disease TEXT NOT NULL,
#             bill INTEGER NOT NULL
#         )
#     """)

#     connection.commit()

#     print("Database and table created successfully")


    
#     patients = [
#         ("Karan Mehta", "9876500011", "Fever", 2500),
#         ("Sneha Kapoor", "9876500022", "Migraine", 4500),
#         ("Vivek Joshi", "9876500033", "Fracture", 8000)
#     ]

#     cursor.executemany("""
#         INSERT INTO patients
#         (name, phone, disease, bill)
#         VALUES (?, ?, ?, ?)
#     """, patients)

#     connection.commit()

#     print("Patients inserted successfully")


    
#     display_all_patients(cursor)


    
#     patient_name = input("\nEnter patient name: ")

#     cursor.execute(
#         "SELECT * FROM patients WHERE name = ?",
#         (patient_name,)
#     )

#     patient = cursor.fetchone()

#     if patient:

#         print("\nPatient Found")

#         print(f"ID: {patient[0]}")
#         print(f"Name: {patient[1]}")
#         print(f"Phone: {patient[2]}")
#         print(f"Disease: {patient[3]}")
#         print(f"Bill: {patient[4]}")

#     else:

#         print("Patient not found")


    

#     cursor.execute(
#         "SELECT id FROM patients WHERE name = ?",
#         ("Karan Mehta",)
#     )

#     karan = cursor.fetchone()

#     if karan:

#         karan_id = karan[0]

#         cursor.execute(
#             "UPDATE patients SET bill = ? WHERE id = ?",
#             (3000, karan_id)
#         )

#         connection.commit()

#         print("\nBill updated successfully")

        

#         cursor.execute(
#             "SELECT * FROM patients WHERE id = ?",
#             (karan_id,)
#         )

#         updated_patient = cursor.fetchone()

#         print(
#             f"ID: {updated_patient[0]} | "
#             f"Name: {updated_patient[1]} | "
#             f"Disease: {updated_patient[3]} | "
#             f"Bill: {updated_patient[4]}"
#         )


    

#     cursor.execute(
#         "DELETE FROM patients WHERE name = ?",
#         ("Vivek Joshi",)
#     )

#     connection.commit()

#     print("\nVivek Joshi deleted successfully")


    

#     print("\n--- Remaining Patients ---")

#     cursor.execute("SELECT * FROM patients")

#     remaining_patients = cursor.fetchall()

#     for patient in remaining_patients:

#         print(
#             f"ID: {patient[0]} | "
#             f"Name: {patient[1]} | "
#             f"Disease: {patient[3]} | "
#             f"Bill: {patient[4]}"
#         )


    

#    get_high_bill_patients(cursor)


# except sqlite3.Error as error:

#     print(f"Database error: {error}")


# finally:

#     if connection:

#         connection.close()



#                                                       Question = 4
# 
# import sqlite3




# def get_premium_orders(cursor):

#     cursor.execute(
#         "SELECT * FROM restaurant_orders WHERE amount > ?",
#         (450,)
#     )

#     premium_orders = cursor.fetchall()

#     print("\n--- Premium Orders ---")

#     for order in premium_orders:
#         print(f"{order[1]} - {order[4]}")


# connection = None

# try:

    
#     connection = sqlite3.connect("food_orders.db")
#     cursor = connection.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS restaurant_orders (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             customer_name TEXT NOT NULL,
#             item TEXT NOT NULL,
#             category TEXT NOT NULL,
#             amount INTEGER NOT NULL
#         )
#     """)

#     connection.commit()

#     print("Database and table created successfully")


    

#     orders = [
#         ("Rahul Sharma", "Biryani", "Indian", 550),
#         ("Neha Gupta", "Noodles", "Chinese", 320),
#         ("Amit Joshi", "Sandwich", "Fast Food", 220),
#         ("Simran Kaur", "Paneer Tikka", "Indian", 480)
#     ]

#     cursor.executemany(
#         """
#         INSERT INTO restaurant_orders
#         (customer_name, item, category, amount)
#         VALUES (?, ?, ?, ?)
#         """,
#         orders
#     )

#     connection.commit()

#     print("Orders inserted successfully")


    

#     print("\n--- All Orders ---")

#     cursor.execute("SELECT * FROM restaurant_orders")

#     all_orders = cursor.fetchall()

#     for order in all_orders:

#         print(
#             f"ID: {order[0]} | "
#             f"Customer: {order[1]} | "
#             f"Item: {order[2]} | "
#             f"Category: {order[3]} | "
#             f"Amount: {order[4]}"
#         )

#     print(f"\nTotal Orders: {len(all_orders)}")


    
#     customer_name = input("\nEnter customer name: ")

#     cursor.execute(
#         """
#         SELECT * FROM restaurant_orders
#         WHERE customer_name = ?
#         """,
#         (customer_name,)
#     )

#     found_order = cursor.fetchone()

#     if found_order:

#         print("\nOrder Found")

#         print(
#             f"ID: {found_order[0]} | "
#             f"Customer: {found_order[1]} | "
#             f"Item: {found_order[2]} | "
#             f"Category: {found_order[3]} | "
#             f"Amount: {found_order[4]}"
#         )

#     else:

#         print("\nOrder not found")


    
#     cursor.execute(
#         """
#         SELECT id
#         FROM restaurant_orders
#         WHERE customer_name = ?
#         """,
#         ("Rahul Sharma",)
#     )

#     rahul_order = cursor.fetchone()

#     if rahul_order:

#         rahul_id = rahul_order[0]

#         cursor.execute(
#             """
#             UPDATE restaurant_orders
#             SET amount = ?
#             WHERE id = ?
#             """,
#             (650, rahul_id)
#         )

#         connection.commit()

#         print("\nAmount updated successfully")


       

#         cursor.execute(
#             """
#             SELECT * FROM restaurant_orders
#             WHERE id = ?
#             """,
#             (rahul_id,)
#         )

#         updated_order = cursor.fetchone()

#         print(
#             f"ID: {updated_order[0]} | "
#             f"Customer: {updated_order[1]} | "
#             f"Item: {updated_order[2]} | "
#             f"Category: {updated_order[3]} | "
#             f"Amount: {updated_order[4]}"
#         )


    
#     cursor.execute(
#         """
#         DELETE FROM restaurant_orders
#         WHERE customer_name = ?
#         """,
#         ("Amit Joshi",)
#     )

#     connection.commit()

#     print("\nAmit Joshi's order deleted successfully")


    

#     print("\n--- Remaining Orders ---")

#     cursor.execute("SELECT * FROM restaurant_orders")

#     remaining_orders = cursor.fetchall()

#     for order in remaining_orders:

#         print(
#             f"ID: {order[0]} | "
#             f"Customer: {order[1]} | "
#             f"Item: {order[2]} | "
#             f"Category: {order[3]} | "
#             f"Amount: {order[4]}"
#         )


    

#     get_premium_orders(cursor)


# except sqlite3.Error as error:

#     print(f"Database error: {error}")


# finally:

#     if connection:
#         connection.close()

#     print("\nDatabase connection closed")




#                                                   questin =5

# import sqlite3



# def get_high_value_products(cursor):

#     cursor.execute(
#         "SELECT * FROM products WHERE price > ?",
#         (1000,)
#     )

#     products = cursor.fetchall()

#     print("\n--- High Value Products ---")

#     for product in products:
#         print(f"{product[1]} - {product[4]}")


# connection = None

# try:

#     connection = sqlite3.connect("store.db")
#     cursor = connection.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS products (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             customer_name TEXT NOT NULL,
#             product TEXT NOT NULL,
#             category TEXT NOT NULL,
#             price INTEGER NOT NULL
#         )
#     """)

#     connection.commit()

#     print("Database and table created successfully")


   
#     products = [
#         ("Arjun Mehta", "Laptop", "Electronics", 55000),
#         ("Kavita Rao", "Headphones", "Electronics", 2500),
#         ("Mohit Jain", "Keyboard", "Accessories", 1800),
#         ("Priya Shah", "Mouse", "Accessories", 900)
#     ]

#     cursor.executemany(
#         """
#         INSERT INTO products
#         (customer_name, product, category, price)
#         VALUES (?, ?, ?, ?)
#         """,
#         products
#     )

#     connection.commit()

#     print("Products inserted successfully")


    
#     cursor.execute("SELECT * FROM products")

#     all_products = cursor.fetchall()

#     print("\n--- All Products ---")

#     for product in all_products:
#         print(
#             f"ID: {product[0]} | "
#             f"Customer: {product[1]} | "
#             f"Product: {product[2]} | "
#             f"Category: {product[3]} | "
#             f"Price: {product[4]}"
#         )

#     print(f"\nTotal Products: {len(all_products)}")


    
#     name = input("\nEnter customer name: ")

#     cursor.execute(
#         "SELECT * FROM products WHERE customer_name = ?",
#         (name,)
#     )

#     found = cursor.fetchone()

#     if found:
#         print("\nProduct Found")
#         print(
#             f"ID: {found[0]} | Customer: {found[1]} | "
#             f"Product: {found[2]} | Category: {found[3]} | "
#             f"Price: {found[4]}"
#         )
#     else:
#         print("\nProduct not found")


    
#     cursor.execute(
#         "SELECT id FROM products WHERE customer_name = ?",
#         ("Arjun Mehta",)
#     )

#     arjun = cursor.fetchone()

#     if arjun:

#         product_id = arjun[0]

#         cursor.execute(
#             "UPDATE products SET price = ? WHERE id = ?",
#             (60000, product_id)
#         )

#         connection.commit()

#         print("\nPrice updated successfully")

#         cursor.execute(
#             "SELECT * FROM products WHERE id = ?",
#             (product_id,)
#         )

#         updated = cursor.fetchone()

#         print(
#             f"ID: {updated[0]} | Customer: {updated[1]} | "
#             f"Product: {updated[2]} | Category: {updated[3]} | "
#             f"Price: {updated[4]}"
#         )


    
#     cursor.execute(
#         "DELETE FROM products WHERE customer_name = ?",
#         ("Priya Shah",)
#     )

#     connection.commit()

#     print("\nPriya Shah's product deleted successfully")


    
#     cursor.execute("SELECT * FROM products")

#     remaining = cursor.fetchall()

#     print("\n--- Remaining Products ---")

#     for product in remaining:
#         print(
#             f"ID: {product[0]} | Customer: {product[1]} | "
#             f"Product: {product[2]} | Category: {product[3]} | "
#             f"Price: {product[4]}"
#         )


    
#     get_high_value_products(cursor)


# except sqlite3.Error as error:
#     print(f"Database error: {error}")

# finally:

#     if connection:
#         connection.close()

#     print("\nDatabase connection closed")

#                                                      Question = 6
# import sqlite3



# def get_high_salary_employees(cursor):

#     cursor.execute(
#         "SELECT * FROM employees WHERE salary > ?",
#         (50000,)
#     )

#     employees = cursor.fetchall()

#     print("\n--- High Salary Employees ---")

#     for employee in employees:
#         print(f"{employee[1]} - {employee[4]}")


# connection = None

# try:

   
#     connection = sqlite3.connect("office.db")
#     cursor = connection.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS employees (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             department TEXT NOT NULL,
#             position TEXT NOT NULL,
#             salary INTEGER NOT NULL
#         )
#     """)

#     connection.commit()

#     print("Database and table created successfully")


#   
#     employees = [
#         ("Rohan Verma", "IT", "Developer", 65000),
#         ("Sneha Kapoor", "HR", "Manager", 58000),
#         ("Vikas Yadav", "Sales", "Executive", 42000),
#         ("Nisha Patel", "IT", "Tester", 47000)
#     ]

#     cursor.executemany(
#         """
#         INSERT INTO employees
#         (name, department, position, salary)
#         VALUES (?, ?, ?, ?)
#         """,
#         employees
#     )

#     connection.commit()

#     print("Employees inserted successfully")


    
#     cursor.execute("SELECT * FROM employees")

#     records = cursor.fetchall()

#     print("\n--- All Employees ---")

#     for employee in records:
#         print(
#             f"ID: {employee[0]} | Name: {employee[1]} | "
#             f"Department: {employee[2]} | Position: {employee[3]} | "
#             f"Salary: {employee[4]}"
#         )

#     print(f"\nTotal Employees: {len(records)}")


#    
#     name = input("\nEnter employee name: ")

#     cursor.execute(
#         "SELECT * FROM employees WHERE name = ?",
#         (name,)
#     )

#     found = cursor.fetchone()

#     if found:
#         print("\nEmployee Found")
#         print(
#             f"ID: {found[0]} | Name: {found[1]} | "
#             f"Department: {found[2]} | Position: {found[3]} | "
#             f"Salary: {found[4]}"
#         )
#     else:
#         print("\nEmployee not found")


   
#     cursor.execute(
#         "SELECT id FROM employees WHERE name = ?",
#         ("Rohan Verma",)
#     )

#     rohan = cursor.fetchone()

#     if rohan:

#         employee_id = rohan[0]

#         cursor.execute(
#             "UPDATE employees SET salary = ? WHERE id = ?",
#             (70000, employee_id)
#         )

#         connection.commit()

#         print("\nSalary updated successfully")

#         cursor.execute(
#             "SELECT * FROM employees WHERE id = ?",
#             (employee_id,)
#         )

#         updated = cursor.fetchone()

#         print(
#             f"ID: {updated[0]} | Name: {updated[1]} | "
#             f"Department: {updated[2]} | Position: {updated[3]} | "
#             f"Salary: {updated[4]}"
#         )


    
#     cursor.execute(
#         "DELETE FROM employees WHERE name = ?",
#         ("Vikas Yadav",)
#     )

#     connection.commit()

#     print("\nVikas Yadav deleted successfully")


    
#     cursor.execute("SELECT * FROM employees")

#     remaining = cursor.fetchall()

#     print("\n--- Remaining Employees ---")

#     for employee in remaining:
#         print(
#             f"ID: {employee[0]} | Name: {employee[1]} | "
#             f"Department: {employee[2]} | Position: {employee[3]} | "
#             f"Salary: {employee[4]}"
#         )


   
#     get_high_salary_employees(cursor)


# except sqlite3.Error as error:
#     print(f"Database error: {error}")

# finally:

#     if connection:
#         connection.close()

#     print("\nDatabase connection closed")






#                                                          Question =7
# import sqlite3



# def get_expensive_books(cursor):

#     cursor.execute(
#         "SELECT * FROM books WHERE price > ?",
#         (500,)
#     )

#     books = cursor.fetchall()

#     print("\n--- Expensive Books ---")

#     for book in books:
#         print(f"{book[1]} - {book[4]}")


# connection = None

# try:

#     # Database
#     connection = sqlite3.connect("library.db")
#     cursor = connection.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS books (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             reader_name TEXT NOT NULL,
#             title TEXT NOT NULL,
#             genre TEXT NOT NULL,
#             price INTEGER NOT NULL
#         )
#     """)

#     connection.commit()

#     print("Database and table created successfully")


    
#     books = [
#         ("Aman Singh", "Python Basics", "Programming", 650),
#         ("Meena Joshi", "Atomic Habits", "Self Help", 450),
#         ("Karan Malhotra", "Clean Code", "Programming", 750),
#         ("Ritu Sharma", "Rich Dad Poor Dad", "Finance", 400)
#     ]

#     cursor.executemany(
#         """
#         INSERT INTO books
#         (reader_name, title, genre, price)
#         VALUES (?, ?, ?, ?)
#         """,
#         books
#     )

#     connection.commit()

#     print("Books inserted successfully")


    
#     cursor.execute("SELECT * FROM books")

#     all_books = cursor.fetchall()

#     print("\n--- All Books ---")

#     for book in all_books:
#         print(
#             f"ID: {book[0]} | Reader: {book[1]} | "
#             f"Title: {book[2]} | Genre: {book[3]} | "
#             f"Price: {book[4]}"
#         )

#     print(f"\nTotal Books: {len(all_books)}")


    
#     reader = input("\nEnter reader name: ")

#     cursor.execute(
#         "SELECT * FROM books WHERE reader_name = ?",
#         (reader,)
#     )

#     found = cursor.fetchone()

#     if found:
#         print("\nBook Found")
#         print(
#             f"ID: {found[0]} | Reader: {found[1]} | "
#             f"Title: {found[2]} | Genre: {found[3]} | "
#             f"Price: {found[4]}"
#         )
#     else:
#         print("\nBook not found")


    
#     cursor.execute(
#         "SELECT id FROM books WHERE reader_name = ?",
#         ("Aman Singh",)
#     )

#     aman = cursor.fetchone()

#     if aman:

#         book_id = aman[0]

#         cursor.execute(
#             "UPDATE books SET price = ? WHERE id = ?",
#             (700, book_id)
#         )

#         connection.commit()

#         print("\nPrice updated successfully")

#         cursor.execute(
#             "SELECT * FROM books WHERE id = ?",
#             (book_id,)
#         )

#         updated = cursor.fetchone()

#         print(
#             f"ID: {updated[0]} | Reader: {updated[1]} | "
#             f"Title: {updated[2]} | Genre: {updated[3]} | "
#             f"Price: {updated[4]}"
#         )


  
#     cursor.execute(
#         "DELETE FROM books WHERE reader_name = ?",
#         ("Ritu Sharma",)
#     )

#     connection.commit()

#     print("\nRitu Sharma's book deleted successfully")


 
#     cursor.execute("SELECT * FROM books")

#     remaining = cursor.fetchall()

#     print("\n--- Remaining Books ---")

#     for book in remaining:
#         print(
#             f"ID: {book[0]} | Reader: {book[1]} | "
#             f"Title: {book[2]} | Genre: {book[3]} | "
#             f"Price: {book[4]}"
#         )


   
#     get_expensive_books(cursor)


# except sqlite3.Error as error:
#     print(f"Database error: {error}")

# finally:

#     if connection:
#         connection.close()

#     print("\nDatabase connection closed")


#                                                      Question =8
#import sqlite3



# def get_high_rent_cars(cursor):

#     cursor.execute(
#         "SELECT * FROM cars WHERE rent > ?",
#         (3000,)
#     )

#     cars = cursor.fetchall()

#     print("\n--- High Rent Cars ---")

#     for car in cars:
#         print(f"{car[1]} - {car[4]}")


# connection = None

# try:

  
#     connection = sqlite3.connect("rental.db")
#     cursor = connection.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS cars (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             customer_name TEXT NOT NULL,
#             car_name TEXT NOT NULL,
#             car_type TEXT NOT NULL,
#             rent INTEGER NOT NULL
#         )
#     """)

#     connection.commit()

#     print("Database and table created successfully")


    
#     cars = [
#         ("Deepak Kumar", "Honda City", "Sedan", 2800),
#         ("Anjali Verma", "Toyota Fortuner", "SUV", 5500),
#         ("Suresh Patel", "Hyundai Creta", "SUV", 3500),
#         ("Pankaj Gupta", "Maruti Swift", "Hatchback", 1800)
#     ]

#     cursor.executemany(
#         """
#         INSERT INTO cars
#         (customer_name, car_name, car_type, rent)
#         VALUES (?, ?, ?, ?)
#         """,
#         cars
#     )

#     connection.commit()

#     print("Cars inserted successfully")


  
#     cursor.execute("SELECT * FROM cars")

#     all_cars = cursor.fetchall()

#     print("\n--- All Cars ---")

#     for car in all_cars:
#         print(
#             f"ID: {car[0]} | Customer: {car[1]} | "
#             f"Car: {car[2]} | Type: {car[3]} | "
#             f"Rent: {car[4]}"
#         )

#     print(f"\nTotal Cars: {len(all_cars)}")


   
#     customer = input("\nEnter customer name: ")

#     cursor.execute(
#         "SELECT * FROM cars WHERE customer_name = ?",
#         (customer,)
#     )

#     found = cursor.fetchone()

#     if found:
#         print("\nBooking Found")
#         print(
#             f"ID: {found[0]} | Customer: {found[1]} | "
#             f"Car: {found[2]} | Type: {found[3]} | "
#             f"Rent: {found[4]}"
#         )
#     else:
#         print("\nBooking not found")


   
#     cursor.execute(
#         "SELECT id FROM cars WHERE customer_name = ?",
#         ("Deepak Kumar",)
#     )

#     deepak = cursor.fetchone()

#     if deepak:

#         car_id = deepak[0]

#         cursor.execute(
#             "UPDATE cars SET rent = ? WHERE id = ?",
#             (3200, car_id)
#         )

#         connection.commit()

#         print("\nRent updated successfully")

#         cursor.execute(
#             "SELECT * FROM cars WHERE id = ?",
#             (car_id,)
#         )

#         updated = cursor.fetchone()

#         print(
#             f"ID: {updated[0]} | Customer: {updated[1]} | "
#             f"Car: {updated[2]} | Type: {updated[3]} | "
#             f"Rent: {updated[4]}"
#         )


   
#     cursor.execute(
#         "DELETE FROM cars WHERE customer_name = ?",
#         ("Pankaj Gupta",)
#     )

#     connection.commit()

#     print("\nPankaj Gupta's booking deleted successfully")


    
#     cursor.execute("SELECT * FROM cars")

#     remaining = cursor.fetchall()

#     print("\n--- Remaining Cars ---")

#     for car in remaining:
#         print(
#             f"ID: {car[0]} | Customer: {car[1]} | "
#             f"Car: {car[2]} | Type: {car[3]} | "
#             f"Rent: {car[4]}"
#         )


    
#     get_high_rent_cars(cursor)


# except sqlite3.Error as error:
#     print(f"Database error: {error}")

# finally:

#     if connection:
#         connection.close()

#     print("\nDatabase connection closed")


#                                                        Question = 9
#  import sqlite3



# def get_high_rent_cars(cursor):

#     cursor.execute(
#         "SELECT * FROM cars WHERE rent > ?",
#         (3000,)
#     )

#     cars = cursor.fetchall()

#     print("\n--- High Rent Cars ---")

#     for car in cars:
#         print(f"{car[1]} - {car[4]}")


# connection = None

# try:

#    
#     connection = sqlite3.connect("rental.db")
#     cursor = connection.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS cars (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             customer_name TEXT NOT NULL,
#             car_name TEXT NOT NULL,
#             car_type TEXT NOT NULL,
#             rent INTEGER NOT NULL
#         )
#     """)

#     connection.commit()

#     print("Database and table created successfully")


#   
#     cars = [
#         ("Deepak Kumar", "Honda City", "Sedan", 2800),
#         ("Anjali Verma", "Toyota Fortuner", "SUV", 5500),
#         ("Suresh Patel", "Hyundai Creta", "SUV", 3500),
#         ("Pankaj Gupta", "Maruti Swift", "Hatchback", 1800)
#     ]

#     cursor.executemany(
#         """
#         INSERT INTO cars
#         (customer_name, car_name, car_type, rent)
#         VALUES (?, ?, ?, ?)
#         """,
#         cars
#     )

#     connection.commit()

#     print("Cars inserted successfully")


#    
#     cursor.execute("SELECT * FROM cars")

#     all_cars = cursor.fetchall()

#     print("\n--- All Cars ---")

#     for car in all_cars:
#         print(
#             f"ID: {car[0]} | Customer: {car[1]} | "
#             f"Car: {car[2]} | Type: {car[3]} | "
#             f"Rent: {car[4]}"
#         )

#     print(f"\nTotal Cars: {len(all_cars)}")


#    
#     customer = input("\nEnter customer name: ")

#     cursor.execute(
#         "SELECT * FROM cars WHERE customer_name = ?",
#         (customer,)
#     )

#     found = cursor.fetchone()

#     if found:
#         print("\nBooking Found")
#         print(
#             f"ID: {found[0]} | Customer: {found[1]} | "
#             f"Car: {found[2]} | Type: {found[3]} | "
#             f"Rent: {found[4]}"
#         )
#     else:
#         print("\nBooking not found")


#     # Update
#     cursor.execute(
#         "SELECT id FROM cars WHERE customer_name = ?",
#         ("Deepak Kumar",)
#     )

#     deepak = cursor.fetchone()

#     if deepak:

#         car_id = deepak[0]

#         cursor.execute(
#             "UPDATE cars SET rent = ? WHERE id = ?",
#             (3200, car_id)
#         )

#         connection.commit()

#         print("\nRent updated successfully")

#         cursor.execute(
#             "SELECT * FROM cars WHERE id = ?",
#             (car_id,)
#         )

#         updated = cursor.fetchone()

#         print(
#             f"ID: {updated[0]} | Customer: {updated[1]} | "
#             f"Car: {updated[2]} | Type: {updated[3]} | "
#             f"Rent: {updated[4]}"
#         )


#     
#     cursor.execute(
#         "DELETE FROM cars WHERE customer_name = ?",
#         ("Pankaj Gupta",)
#     )

#     connection.commit()

#     print("\nPankaj Gupta's booking deleted successfully")


#    
#     cursor.execute("SELECT * FROM cars")

#     remaining = cursor.fetchall()

#     print("\n--- Remaining Cars ---")

#     for car in remaining:
#         print(
#             f"ID: {car[0]} | Customer: {car[1]} | "
#             f"Car: {car[2]} | Type: {car[3]} | "
#             f"Rent: {car[4]}"
#         )


#    
#     get_high_rent_cars(cursor)


# except sqlite3.Error as error:
#     print(f"Database error: {error}")

# finally:

#     if connection:
#         connection.close()

#     print("\nDatabase connection closed")

#                                 question =10
# import sqlite3



# def get_expensive_rooms(cursor):

#     cursor.execute(
#         "SELECT * FROM rooms WHERE price > ?",
#         (4000,)
#     )

#     rooms = cursor.fetchall()

#     print("\n--- Expensive Rooms ---")

#     for room in rooms:
#         print(f"{room[1]} - {room[4]}")


# connection = None

# try:

   
#     connection = sqlite3.connect("hotel.db")
#     cursor = connection.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS rooms (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             guest_name TEXT NOT NULL,
#             room_type TEXT NOT NULL,
#             hotel_name TEXT NOT NULL,
#             price INTEGER NOT NULL
#         )
#     """)

#     connection.commit()

#     print("Database and table created successfully")


#    
#     rooms = [
#         ("Vivek Sharma", "Deluxe", "Royal Palace", 4200),
#         ("Neha Singh", "Standard", "City View", 2800),
#         ("Raj Malhotra", "Suite", "Grand Hotel", 6500),
#         ("Kiran Patel", "Deluxe", "Lake Resort", 3900)
#     ]

#     cursor.executemany(
#         """
#         INSERT INTO rooms
#         (guest_name, room_type, hotel_name, price)
#         VALUES (?, ?, ?, ?)
#         """,
#         rooms
#     )

#     connection.commit()

#     print("Rooms inserted successfully")


    
#     cursor.execute("SELECT * FROM rooms")

#     all_rooms = cursor.fetchall()

#     print("\n--- All Rooms ---")

#     for room in all_rooms:
#         print(
#             f"ID: {room[0]} | Guest: {room[1]} | "
#             f"Room: {room[2]} | Hotel: {room[3]} | "
#             f"Price: {room[4]}"
#         )

#     print(f"\nTotal Rooms: {len(all_rooms)}")


#   
#     guest = input("\nEnter guest name: ")

#     cursor.execute(
#         "SELECT * FROM rooms WHERE guest_name = ?",
#         (guest,)
#     )

#     found = cursor.fetchone()

#     if found:
#         print("\nBooking Found")
#         print(
#             f"ID: {found[0]} | Guest: {found[1]} | "
#             f"Room: {found[2]} | Hotel: {found[3]} | "
#             f"Price: {found[4]}"
#         )
#     else:
#         print("\nBooking not found")


    
#     cursor.execute(
#         "SELECT id FROM rooms WHERE guest_name = ?",
#         ("Vivek Sharma",)
#     )

#     vivek = cursor.fetchone()

#     if vivek:

#         room_id = vivek[0]

#         cursor.execute(
#             "UPDATE rooms SET price = ? WHERE id = ?",
#             (4600, room_id)
#         )

#         connection.commit()

#         print("\nRoom price updated successfully")

#         cursor.execute(
#             "SELECT * FROM rooms WHERE id = ?",
#             (room_id,)
#         )

#         updated = cursor.fetchone()

#         print(
#             f"ID: {updated[0]} | Guest: {updated[1]} | "
#             f"Room: {updated[2]} | Hotel: {updated[3]} | "
#             f"Price: {updated[4]}"
#         )


#  
#     cursor.execute(
#         "DELETE FROM rooms WHERE guest_name = ?",
#         ("Neha Singh",)
#     )

#     connection.commit()

#     print("\nNeha Singh's booking deleted successfully")


#   
#     cursor.execute("SELECT * FROM rooms")

#     remaining = cursor.fetchall()

#     print("\n--- Remaining Rooms ---")

#     for room in remaining:
#         print(
#             f"ID: {room[0]} | Guest: {room[1]} | "
#             f"Room: {room[2]} | Hotel: {room[3]} | "
#             f"Price: {room[4]}"
#         )


    
#     get_expensive_rooms(cursor)


# except sqlite3.Error as error:
#     print(f"Database error: {error}")

# finally:

#     if connection:
#         connection.close()

#     print("\nDatabase connection closed")