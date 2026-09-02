from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Customer, Product


def create_customer(
    session: Session,
    name,
    email,
    phone,
    city
):
    customer = Customer(
        name=name,
        email=email,
        phone=phone,
        city=city
    )

    session.add(customer)
    session.commit()
    session.refresh(customer)

    return customer


def create_product(
    session: Session,
    name,
    price,
    stock_quantity,
    category
):
    product = Product(
        name=name,
        price=price,
        stock_quantity=stock_quantity,
        category=category
    )

    session.add(product)
    session.commit()
    session.refresh(product)

    return product


def get_products(session: Session):
    statement = select(Product)

    products = session.scalars(statement).all()

    return products


def update_stock(
    session: Session,
    product_id,
    quantity
):
    product = session.get(Product, product_id)

    if product is None:
        return None

    product.stock_quantity = quantity

    session.commit()
    session.refresh(product)

    return product


def delete_product(
    session: Session,
    product_id
):
    product = session.get(Product, product_id)

    if product is None:
        return False

    session.delete(product)
    session.commit()

    return True