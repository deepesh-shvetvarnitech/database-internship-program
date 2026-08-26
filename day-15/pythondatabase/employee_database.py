import sqlite3
connection = sqlite3.connect("company.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
      id           INTEGER PRIMARY KEY AUTOINCREMENT,
      name         TEXT    NOT NULL,
      email        TEXT    UNIQUE NOT NULL,
      department   TEXT    NOT NULL,
      salary       INTEGER NOT NULL
  )
 """)
connection.commit()
print("database and table created successfully")
employees = [
    ("Rahul Sharma", "rahul@gmail.com","IT",35000),
    ("Priya Singh", "priya@gmail.com","HR",32000),
    ("Amit Verma", "amit@gmail.com","Sales",30000)
]
cursor.executemany("""
     INSERT INTO employees(name,email,department,salary)
     VALUES(?,?,?,?)""",employees)
connection.commit()
print("Employees inserted successfully")
cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()
for employee in employees:
    print(
        f"|ID :{employee[0]} |"
        f"|Name :{employee[1]} |"
        f"|Email :{employee[2]} |"
        f"|Department:{employee[3]} |"
        f"|Salary :{employee[4]} |"
    )
print(f"Total Employees :{len(employees)}") 
connection.close()
name = input("Enter employees name :")   
cursor.execute("""
       SELECT * FROM employees
       WHERE name = ?
""",(name))
employee = cursor.fetchone()
if employee:
    print("Employee Found")
    print(f"ID :{employee[0]}")
    print(f"Name :{employee[1]}")
    print(f"Email :{employee[2]}")
    print(f"Department :{employee[3]}")
    print(f"Salary :{employee[4]}")
else:
    print("Employee not found")
cursor.execute("""
    SELECT ID FROM employees WHERE name = ?""",("Rahul Sharma",))
rahul = cursor.fetchone()
if rahul:
    rahul_id = rahul[0] 
    cursor.execute("""
       UPDATE employees
       SET salary = ?
       WHERE id   =  ?
       """,(40000,rahul_id))
cursor.execute("""
      SELECT * FROM employees WHERE id = ?""",(rahul_id))
updated_employee  = cursor.fetchone()
print("Salary updated successfully")
print(f"ID :{updated_employee[0]}")
print(f"Name{updated_employee[1]}")
print(f"Email{updated_employee[2]}")
print(f"Department{updated_employee[3]}")
print(f"Salary{updated_employee[4]}")
cursor.execute("""
      DELETE FROM employees WHERE name = ?""",("Amit Verma",))
connection.commit()
print("Employee deleted successfully ")
cursor.execute("SELECT * FROM employees")
remaining_employees = cursor.fetchall()
print("Remianing Employees : ")
for employee in remaining_employees:
    print(employee[0])
connection.close()  


import sqlite3
def get_high_salary_employees(cursor):
    """
    Salary greater than 30000 wale employees find karta hai"""
    cursor.execute("""
    SELECT name,salary FROM employees WHERE salary > ?
""",(30000,))
    employees = cursor.fetchall()
    print("High Salary Employees")
    for employee in employees:
        print(f"{employee[0]}-{employee[1]}")
    return employees    
def  main():
    connection = None
    try:
        connection = sqlite3.connect("company.db")
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name         TEXT    NOT NULL,
               email        TEXT    UNIQUE NOT NULL,
               department   TEXT    NOT NULL,
               salary       INTEGER NOT NULL
         )
 """)
        connection.commit()
        print("database and table created successfully")
        employees = [
             ("Rahul Sharma", "rahul@gmail.com","IT",35000),
             ("Priya Singh", "priya@gmail.com","HR",32000),
             ("Amit Verma", "amit@gmail.com","Sales",30000)
]
        cursor.executemany("""
           INSERT INTO employees(name,email,department,salary)
           VALUES(?,?,?,?)""",employees)
        connection.commit()
        print("Employees inserted successfully")
cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()
print("All Employees")
for employee in employees:
    print(
        f"|ID :{employee[0]} |"
        f"|Name :{employee[1]} |"
        f"|Email :{employee[2]} |"
        f"|Department:{employee[3]} |"
        f"|Salary :{employee[4]} |"
    )
print(f"Total Employees :{len(employees)}") 
name =  input("Enter employee name")
cursor.execute("""
      SELECT * FROM employees WHERE name = ?""",(name))
employee = cursor.fetchone()
if employee:
    print("Employee Found")
    print(f"ID :{employee[0]}")
    print(f"Name :{employee[1]}")
    print(f"Email :{employee[2]}")
    print(f"Department :{employee[3]}")
    print(f"Salary :{employee[4]}")
else:
    print("Employee not found")
    cursor.execute("""
        SELECT ID FROM employees WHERE name = ?""",("Rahul Sharma",))
    rahul = cursor.fetchone()
    if rahul:
        rahul_id = rahul[0] 
        cursor.execute("""
           UPDATE employees
           SET salary = ?
           WHERE id   =  ?
           """,(40000,rahul_id))
        connection.commit()
        cursor.execute("""

        SELECT * FROM employees WHERE id = ?""",(rahul_id))
        updated_employee  = cursor.fetchone()
        print("Salary updated successfully")
        print(f"ID :{updated_employee[0]}")
        print(f"Name{updated_employee[1]}")
        print(f"Email{updated_employee[2]}")
        print(f"Department{updated_employee[3]}")
        print(f"Salary{updated_employee[4]}")
        cursor.execute("""
              DELETE FROM employees WHERE name = ?""",("Amit Verma",))
        connection.commit()
        print("Employee deleted successfully ")
        cursor.execute("SELECT * FROM employees")
        remaining_employees = cursor.fetchall()
        print("Remianing Employees : ")
        for employee in remaining_employees:
            print(employee[1])
        get_high_salary_employees(cursor)
except sqlite3.Error as error:
      print(f"Database error: {error}")

    finally:
        if connection:
            connection.close()

            print("Database connection closed")


if __name__ == "__main__":
            main()