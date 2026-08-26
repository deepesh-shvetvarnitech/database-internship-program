'''
                                            SECTION = A
create_engine()
DeclarativeBase
ORM Models
Column / mapped_column
Data types: Integer, String, Float, Text, Boolean, DateTime
primary_key
nullable
unique
default
ForeignKey
Relationships
Base.metadata.create_all()
inspect()
SQL generation
SQLite database
Multiple model files ko import karna
try/except error handling

                                                     SECION =B
                                                     QUESTION = 1
SQLAlchemy Core database ke saath low-level way me kaam karta hai. Isme hum SQL statements aur tables ke saath directly kaam kar sakte hain.

SQLAlchemy ORM Python classes ko database tables se connect karta hai. Isme hum Python objects ke through database data handle karte hain.

Core: Jab hume direct SQL aur database-level control chahiye.
ORM: Jab backend project me Python classes aur objects ke through database handle karna ho.

                                        QUESTION =2
Declarative Base ek base class hoti hai jiske through hum SQLAlchemy ke ORM models banate hain.

Hum apne models ko is Base class se inherit karte hain. SQLAlchemy Base ke through models ki table information ko manage karta hai.          

                                        QUESTION = 3
SQLAlchemy model ek Python class hoti hai jo database table ko represent karti hai.

Model banane ke liye mainly 3 cheezein hoti hain:

Class name — model ka naam
__tablename__ — database table ka naam
Columns — table ke columns

                                              QUESTION = 4
SQLAlchemy models ki information se database tables create kar sakta hai.

Iske liye hum:

Base.metadata.create_all(engine)

use karte hain.

Base.metadata me models aur unki table information hoti hai.

create_all(engine) database engine se connect karke required tables create karta hai.

Example:

engine = create_engine("sqlite:///store.db")

Base.metadata.create_all(engine)

                                                 SECTION = C
                                                 QUESTION = 1'''
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///store.db")
Base = declarative_base()

print("Engine and Base created successfully")

#                 Question 2

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    age = Column(Integer)
    city = Column(String(100))
    created_at = Column(DateTime, default=datetime.now)

#         Question 3

from sqlalchemy import Column, Integer, String, Text, Float

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    category = Column(String(50))

# Question 4

from sqlalchemy import inspect

Base.metadata.create_all(engine)

print("Tables created successfully")

inspector = inspect(engine)
tables = inspector.get_table_names()

print(tables)


#                                        SECTION = D
#                                            QUESTION =1
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    phone = Column(String(20))
    city = Column(String(100))
    created_at = Column(DateTime, default=datetime.now)

    orders = relationship("Order", back_populates="user")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    category = Column(String(50))
    created_at = Column(DateTime, default=datetime.now)

    __table_args__ = (
        CheckConstraint("price > 0", name="check_price_positive"),
    )

    order_items = relationship("OrderItem", back_populates="product")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String(50), default="pending")
    created_at = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

#                                              Question 2 

import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.schema import CreateTable
from models import Base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///store.db")

engine = create_engine(DATABASE_URL)

try:
    Base.metadata.create_all(engine)

    print("Tables created successfully")

    inspector = inspect(engine)
    tables = inspector.get_table_names()

    print("\nTables:")
    for table in tables:
        print(table)

    print("\nColumns:")
    for table in tables:
        print(table)
        for column in inspector.get_columns(table):
            print(column["name"], column["type"])

    print("\nForeign Keys:")
    for table in tables:
        for fk in inspector.get_foreign_keys(table):
            print(table, "->", fk["referred_table"])

    print("\nSQL:")

    with open("schema.sql", "w", encoding="utf-8") as file:
        for table in Base.metadata.sorted_tables:
            sql = str(CreateTable(table).compile(engine))
            print(f"\n-- {table.name}")
            print(sql)
            file.write(f"-- {table.name}\n")
            file.write(sql)
            file.write(";\n\n")

    print("\nschema.sql created successfully")

except Exception as e:
    print("Database setup failed:", e)                                     
