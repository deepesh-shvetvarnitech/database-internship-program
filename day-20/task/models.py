from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column , Integer,String,Float 
class Base(DeclarativeBase):
    pass
class Product(Base):
    __tablename__ ="products"
    id = Column(Integer,primary_key=True)
    name = Column(String(150),nullable=False)
    price = Column(Float,nullable=False)
    stock_quantity = Column(Integer,default=0)
    category = Column(String(100),nullable=False)
