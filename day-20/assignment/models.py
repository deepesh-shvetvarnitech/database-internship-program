from sqlalchemy import create_engine,Column,Integer,String,Float,inspect 
from sqlalchemy.orm  import declarative_base
try:
    engine = create_engine("sqlite:///store.db")
    print("Engine Created Successfully ")
    Base = declarative_base()
    print("Base created  successfully")
    class Customer(Base):
        __tablename__ = "customers"
        id = Column(Integer,primary_key=True)
        name = Column(String(100),nullable=False)
        email = Column(String(100),nullable=False,unique=True)
        city = Column(String(100),nullable=True)
    class Product(Base):
        __tablename__ ="products"
        id = Column(Integer,primary_key=True)
        name = Column(String(150),nullable=False) 
        price = Column(Float,nullable=False)  
        stock_quantity = Column(Integer,default=0)
        category =  Column(String(50),nullable=True)
    Base.metadata.create_all(engine)  
    print("Tables Created Successfully")
    table_names = Base.metadata.tables.keys()
    print(f"Tables regitered in matadata  :{''.join(table_names)}") 
    inspector = inspect(engine)
    database_tables = inspector.get_table_names()
    print((f"Dtabase Tables  :{''.join(database_tables)}") )
except Exception as e:
    print(f"Error :{str(e)}")
