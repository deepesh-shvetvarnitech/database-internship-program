
           
import sqlite3



connection = None

try:
   
    connection = sqlite3.connect("store.db")
    cursor = connection.cursor()

   
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price INTEGER NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    print("Database and table created successfully")


   

    products = [
        ("Laptop", "Electronics", 55000, 10),
        ("Office Chair", "Furniture", 7500, 5),
        ("Keyboard", "Electronics", 1500, 20)
    ]

    cursor.executemany("""
        INSERT INTO products (name, category, price, stock)
        VALUES (?, ?, ?, ?)
    """, products)

    connection.commit()

    print("Products inserted successfully")


    

    cursor.execute("SELECT * FROM products")

    all_products = cursor.fetchall()

    print("\n=== All Products ====")

    for product in all_products:
        print(
            f"ID: {product[0]} | "
            f"Product: {product[1]} | "
            f"Category: {product[2]} | "
            f"Price: {product[3]} | "
            f"Stock: {product[4]}"
        )

    print(f"\nTotal Products: {len(all_products)}")



    product_name = input("\nEnter product name: ")

    cursor.execute(
        "SELECT * FROM products WHERE name = ?",
        (product_name,)
    )

    product = cursor.fetchone()

    if product:
        print("\nProduct Found")
        print(f"ID: {product[0]}")
        print(f"Name: {product[1]}")
        print(f"Category: {product[2]}")
        print(f"Price: {product[3]}")
        print(f"Stock: {product[4]}")
    else:
        print("Product not found")


   
    cursor.execute(
        "SELECT id FROM products WHERE name = ?",
        ("Laptop",)
    )

    laptop = cursor.fetchone()

    if laptop:
        laptop_id = laptop[0]

      
        cursor.execute(
            "UPDATE products SET stock = ? WHERE id = ?",
            (25, laptop_id)
        )

      
        connection.commit()

        print("\nStock updated successfully")

        cursor.execute(
            "SELECT * FROM products WHERE id = ?",
            (laptop_id,)
        )

        updated_laptop = cursor.fetchone()

       
        print(
            f"ID: {updated_laptop[0]} | "
            f"Product: {updated_laptop[1]} | "
            f"Category: {updated_laptop[2]} | "
            f"Price: {updated_laptop[3]} | "
            f"Stock: {updated_laptop[4]}"
        )
    else:
        print("Laptop not found")


   
    cursor.execute(
        "DELETE FROM products WHERE name = ?",
        ("Keyboard",)
    )

    connection.commit()

    print("\nProduct deleted successfully")

   
    cursor.execute("SELECT * FROM products")

    remaining_products = cursor.fetchall()

    print("\n=== Remaining Products ===")

    for product in remaining_products:
        print(
            f"ID: {product[0]} | "
            f"Product: {product[1]} | "
            f"Category: {product[2]} | "
            f"Price: {product[3]} | "
            f"Stock: {product[4]}"
        )


    
    def get_low_stock_products():
        cursor.execute(
            "SELECT name, stock FROM products WHERE stock < ?",
            (10,)
        )

        low_stock_products = cursor.fetchall()

        print("\n=== Low Stock Report ===")

        if low_stock_products:
            for product in low_stock_products:
                print(f"{product[0]} - Stock: {product[1]}")
        else:
            print("No products need restocking")


    
    get_low_stock_products()


except sqlite3.Error as error:
    print(f"SQLite Error: {error}")


finally:
   
    if connection:
        connection.close()
        print("\nDatabase connection closed")