'''
                                      SECTION = A
                                      QUESTION = 1
SQLAlchemy ORM PYTHON  OBJECT /CLASSE KO DATABSE TABLE SE CONNECT KARE KA TARIKA HAI.HUM MANUlY CREATE TABLE LIKHNE K  BAJYEPYTHON CLASS BNA SAKTE HAI.
                                       QUESTION = 2
                                       create_engine()
CREATE ENGINEDTABSE K SATH KA CONNECTION CONFIGUATION KA ENGINE BNATA HAI . YE SQLalchemy ko bata hai ki konse database se baaat karne hai
 
                                        QUESTION = 3
                                        Base = declarative_base()
BASE EK COMMON PARENT CLASS BNANTA HAI JISSE HMARE ORM MODEL INHERIT KAR SAKE 

                                    QUESTION =4
                                    class Customer(Base):
    __tablename__ = "customers"
  
yha customer pythhon ki class hai or customer database taable ka naam hai .matlab cutomer class -> customer table


                                       QUESTION =5
YE SQLALCHEMY KO BOLTA HAI KI BASE SE CONNECTED MODELS KI TABLE DATABADE M CREATE KARO
AGAR CUSTOMER OR PRODUCT MODELA DEFINED HA . TO UNKI TABLES CREATE HONGI 
METTABLES K ANDER TABLES KI INFORMATION STORE HOTE HAI
ENGINE BATA HAIKI TABLE KIS DATABASE MAIN KARNE HAI
'''
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

'''
                                      QUESTION = 1
SQLAlchemy model ek Python class hoti hai. Ye database table ko represent karti hai. Python class ke through hum database table ka structure aur columns define karte hain.                                      

                                       QUESTION =2
                                 Base.metadata.create_all(engine)
Ye database mein model ke according table create karta hai. Agar table pehle se bani hui hai, toh dobara nahi banata.

                                       QUESTION = 3
  Isse same email dobara database mein insert nahi ho sakti. Matlab duplicate email ko rokta hai.                                     

















'''