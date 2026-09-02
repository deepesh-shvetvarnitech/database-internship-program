import sqlite3

try:
    conn = sqlite3.connect("inventory_demo.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    products = [
        ("Laptop", 65000, 10),
        ("Keyboard", 2500, 25),
        ("Mouse", 1200, 40),
        ("Monitor", 15000, 8)
    ]

    cursor.executemany(
        "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
        products
    )

    conn.commit()

    cursor.execute("SELECT * FROM products")
    all_products = cursor.fetchall()

    print("All Products:")
    for product in all_products:
        print(product)

    product_name = input("Enter product name: ")

    cursor.execute(
        "SELECT * FROM products WHERE name = ?",
        (product_name,)
    )

    product = cursor.fetchone()

    print("\nSearch Result:")
    print(product)

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if cursor:
        cursor.close()

    if conn:
        conn.close()

    print("SQLite connection closed")