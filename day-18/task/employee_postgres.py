'''
                                             SECTION = A
                                             qUESTION = 1
POSTGRE SQL CONNECTION IS REQUIRED BEFORE CURD OPERATOINS BECAUSE IT ALLOWS PYTHON TO COMMUNICATE WITH THE POSTGRESQL DATABASE
AFTER CREATING CONNECTION WE CREATE CURSOR,THEN THROUGH CURSER EXECUTE  QUERIES

                                             QUESTION = 2
WITH CONNECTION WE MANAGES THE TRANSACTION 
EX
WITH CONNECTION 
      WITH CONNECTION.CURSOR()AS CURSOR:
      CURSOR.EXECUTE(SELECT*FROM EMPLOYEE)
                                             QUESTION = 3
A CONTEXT MANAGER SUCH AS WITHCONNECTION.COURSOR ()AS CURSOR HEL SAFELY MANGE DATABASE  RESOURSES
IT AUTOMATICALLY HE=ANDLES THE CURSOR LIFECYCLCLE AND MANAGE

                                             QUESTION = 4
POSTGRESQL OPERATION SHOULD BE PLACED   INSIDE TRY EXCEPT  BECAUSE DATABSE OPERTIONS FAIL DUE TO CONNECTION PROBLEMS ,INVALID SQL DUPLICATE DATA OR CONSTRAIT VOILATION .


                                             '''
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}


def get_connection():
    connection = psycopg2.connect(
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    return connection


def test_connection():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT 1")
        result = cursor.fetchone()

        print("Connection:", result)
        print("Database connection successful")

        cursor.close()
        connection.close()

    except Exception as error:
        print("Connection failed")


def create_table():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(150) UNIQUE NOT NULL,
                department VARCHAR(100) NOT NULL,
                salary INTEGER NOT NULL
            )
        """)

        connection.commit()

        print("Table created successfully")

        cursor.close()
        connection.close()

    except psycopg2.Error as error:
        print("Table error:", error)


def insert_employees():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        employees = [
            ("Rahul Sharma", "rahul@example.com", "IT", 45000),
            ("Priya Singh", "priya@example.com", "HR", 40000),
            ("Amit Verma", "amit@example.com", "Sales", 35000)
        ]

        for employee in employees:
            cursor.execute("""
                INSERT INTO employees
                (name, email, department, salary)
                VALUES (%s, %s, %s, %s)
            """, employee)

        connection.commit()

        print("Employees inserted")

        cursor.close()
        connection.close()

    except psycopg2.Error as error:
        print("Insert error")


def get_employees():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, name, department, salary
            FROM employees
        """)

        employees = cursor.fetchall()

        print("\nEmployees")

        for employee in employees:
            print(
                employee[0],
                employee[1],
                employee[2],
                employee[3]
            )

        cursor.close()
        connection.close()

    except psycopg2.Error as error:
        print("Select error")


def update_rahul_salary():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE employees
            SET salary = 50000
            WHERE email = %s
        """, ("rahul@example.com",))

        connection.commit()

        print("Salary updated")

        cursor.close()
        connection.close()

    except psycopg2.Error as error:
        print("Update error")


def delete_amit():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM employees
            WHERE email = %s
        """, ("amit@example.com",))

        connection.commit()

        print("Employee deleted")

        cursor.close()
        connection.close()

    except psycopg2.Error as error:
        print("Delete error")


def remaining_employees():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT name, department, salary
            FROM employees
        """)

        employees = cursor.fetchall()

        print("\nRemaining Employees")

        for employee in employees:
            print(
                employee[0],
                employee[1],
                employee[2]
            )

        cursor.close()
        connection.close()

    except psycopg2.Error as error:
        print("Report error")


if __name__ == "__main__":
    test_connection()
    create_table()
    insert_employees()
    get_employees()
    update_rahul_salary()
    delete_amit()
    remaining_employees()
                   
    