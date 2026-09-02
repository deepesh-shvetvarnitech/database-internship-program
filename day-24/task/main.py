from sqlalchemy import select
from database import(
    SessionLocal,
    engine,
    test_connection

)
from models import Base , Customer , Order
from curd import(
    create_customer,
    create_product,
    get_product,
    update_stock,
    delete_product
)
def main():
    print("="*40)
    print("INVENTORY AND ORDER MANAGMENT SYSTEM")
    print("="*40)
    test_connection()
    Base.metadata.create_all(engine)
    print("Database Created Successfully")
    session = SessionLocal()
    try:
        customer = create_customer(
            session,
            "Rahul Sharma",
            "rahul@gmail.com",
            "9876543210"
            "Indore"
        )
        print(
            f"Customer Created Successfully: "
            f"|{customer.id}|"
            f"|{customer.name}|"
            f"|{customer.email}|"
        )
        laptop = create_product(
            session,
            "Laptop",
            65000,
            10,
            "Electronics"
        )
        keyboard = create_product(
                    session,
                    "keyboard",
                    25000,
                    25,
                    "Accessories"
                )
        mouse = create_product(
                            session,
                            "Mouse",
                            1200,
                            40,
                            "Accessories"
                        )
        monitor = create_product(
                    session,
                    "Monitor",
                    15000,
                    8,
                    "Electronics"
                )
        print("Product Created successfully")
        products = get_product(session)
        for product in products:
            print(
                f"|{product.id}|",
                f"|{product.name}|",
                f"|{product.price}|",
                f"Stock : {product.Stock_quantity}
            )

            
        order1 = Order(
            customer_id = customer.id,
            total_amount = 675000,
            status = "pending"
        )
        order2 = Order(
                    customer_id = customer.id,
                    total_amount = 15000,
                    status = "completed"
                )  
        session.add_all([order1,order2])
        session.commit()
        session.refresh(order1) 
        session.refresh(order2)                            
        print("Order Created Successfully")
        print(
            f"|Order #{order1.id}|",
            f"|{customer.name}|",
            f"|{order1.total_amount}|",
            f"|{order1.status}|"
        ) 
        print(
            f"|Order #{order2.id}|",
            f"|{customer.name}|",
            f"|{order2.total_amount}|",
            f"|{order2.status}|"
        ) 
        print("Upadating Mouce  Stock")  
        updated_mouse =update_stock(
            session ,
            mouse.id
        )
        print(
            f"Stock Updated Successfully"
            f"|{updated_mouse.name}|"
            f"Stock : {updated_mouse.stock_quantity}"

        ) 
        print("deleted product")
        deleted = delete_product (
            session,
            monitor.id
        )
        if deleted:
           print("Product Deleted Successfully")
        print("\n"+ "="*40)
        print("TRANSACTION TEST")
        print( "="*40)  
        try:
            Invalid_customer = Customer(
            name = None ,
            email = None
            )
            session.add(Invalid_customer) 
            session.commit()
        except Exception as error:
                session.rollback()
                print("Database error Occured")
                print("Rollback performed Successfully")
        print("\n"+ "="*40)
        print("CUSTOMERS ORDERS")
        print( "="*40) 
        statement = select(Customer).where(
             Customer.email== "rahul@gmail.com"

        )             
        rahul = session .scalar(statement)
        print(f"{rahul.name}")
        for order in rahul.orders:
            print(
                f"Order # {order.id}"
                f"Amount : {order.total_amount}"
                f"Status : {order.status}"
            ) 
except Exception as error:
        session.rollback()
        print(f"application error : {error}")
finally:
         session.close()
         print("session close successfully")
if __name__ == "__main__":
         main()                                                  
                                             