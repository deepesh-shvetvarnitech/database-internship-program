'''
#                                           SECTION = A
# 1) A workspace for tracking object changes
# 2) sessionmaker
# 3) session.add()
# 4) session.commit()
# 5) session.rollback()
# 6) session.close()
# 7) All changes are saved to database
# 8) All uncommitted changes are discarded
# 9) session.query() or session.execute()
# 10) session.delete()
# 11) Reloads object state from database
# 12) Create, Read, Update, Delete
# 13) A unit of work that is committed or rolled back
# 14) After completing a set of related changes
# 15) Changes are not saved
# 16) try/finally with session.close()
# 17) Adds multiple objects to session
# 18) session.get(Model, id)
# 19) Send pending changes to database without committing
# 20) Use short-lived sessions per operation    

#                                           SECTION = B
#                                           QUESTION = 1
# QLAlchemy Session ka lifecycle mainly ye hota hai:

# Session create karte hain.
# Session ke through database operation karte hain.
# Successful operation ke baad commit() karte hain.
# Error aaye to rollback() karte hain.
# Finally session ko close() karte hain.

#                                          QUESTION =2
# commit() database me changes ko permanently save karta hai.

# rollback() uncommitted changes ko cancel karta hai jab operation me error aaye.

#                                          QUESTION = 3
# Session manage karte time:

# Kaam complete hone ke baad session close karna chahiye.
# Error hone par rollback() karna chahiye.
# Session ko unnecessarily long time tak open nahi rakhna chahiye.
#                                          QUESTION = 4
# Database operation ko try block me rakhte hain. Agar error aaye to except me rollback() karte hain. finally me session ko close() karte hain.

# session = SessionLocal()

# try:
#     session.add(user)
#     session.commit()
# except Exception as e:
#     session.rollback()
#     print("Error:", e)
# finally:
#     session.close()
#                                        SECTION = C
#                                        QUESTION =1'''
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session, sessionmaker

# engine = create_engine("sqlite:///store.db")

# SessionLocal = sessionmaker(bind=engine)

# session = SessionLocal()
# #                                           QUESTION =2
# from contextlib import contextmanager

# @contextmanager
# def get_session():
#     session = SessionLocal()

#     try:
#         yield session
#         session.commit()
#     except Exception:
#         session.rollback()
#         raise
#     finally:
#         session.close()
      
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# engine = create_engine("sqlite:///store.db")

# SessionLocal = sessionmaker(bind=engine)

# from contextlib import contextmanager
# from database import SessionLocal

# @contextmanager
# def get_session():
#     session = SessionLocal()

#     try:
#         yield session
#         session.commit()
#     except Exception:
#         session.rollback()
#         raise
#     finally:
#         session.close() 
#         ''' ISME TIN BNANE PADTE ISKIYE EK M KAR DIYE'''
# #QUESTION =3
# from session_manager import get_session

# with get_session() as session:
#     print("Session created successfully")
#     print(session is not None)

# #                                              QUESTION =4
# from sqlalchemy import text
# from database import SessionLocal

# session = SessionLocal()

# try:
#     session.execute(text("SELECT 1"))
#     session.commit()
#     print("Operation successful")
# except Exception as e:
#     session.rollback()
#     print("Error:", e)
# finally:
#     session.close()

# #                                                 SECTION = D
# from sqlalchemy import create_engine, Integer, String, Float
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# class Base(DeclarativeBase):
#     pass

# class User(Base):
#     __tablename__ = "users"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String(100), nullable=False)
#     email: Mapped[str] = mapped_column(String(150), nullable=False)
#     password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
#     phone: Mapped[str] = mapped_column(String(20))
#     city: Mapped[str] = mapped_column(String(100))

# class Product(Base):
#     __tablename__ = "products"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String(150), nullable=False)
#     description: Mapped[str] = mapped_column(String(255))
#     price: Mapped[float] = mapped_column(Float, nullable=False)
#     stock_quantity: Mapped[int] = mapped_column(Integer, default=0)
#     category: Mapped[str] = mapped_column(String(100))

# engine = create_engine("sqlite:///store.db")
# SessionLocal = sessionmaker(bind=engine)

# Base.metadata.create_all(engine)
# crud_operations.py
# from models import User, Product

# def create_user(session, name, email, password_hash, phone, city):
#     try:
#         user = User(
#             name=name,
#             email=email,
#             password_hash=password_hash,
#             phone=phone,
#             city=city
#         )
#         session.add(user)
#         session.commit()
#         session.refresh(user)
#         return user
#     except Exception:
#         session.rollback()
#         raise

# def create_product(session, name, description, price, stock_quantity, category):
#     try:
#         product = Product(
#             name=name,
#             description=description,
#             price=price,
#             stock_quantity=stock_quantity,
#             category=category
#         )
#         session.add(product)
#         session.commit()
#         session.refresh(product)
#         return product
#     except Exception:
#         session.rollback()
#         raise

# def get_user_by_id(session, user_id):
#     return session.get(User, user_id)

# def get_all_users(session):
#     return session.query(User).all()

# def get_product_by_id(session, product_id):
#     return session.get(Product, product_id)

# def update_user(session, user_id, **kwargs):
#     user = session.get(User, user_id)

#     if not user:
#         return None

#     try:
#         for key, value in kwargs.items():
#             if hasattr(user, key):
#                 setattr(user, key, value)

#         session.commit()
#         session.refresh(user)
#         return user
#     except Exception:
#         session.rollback()
#         raise

# def update_product(session, product_id, **kwargs):
#     product = session.get(Product, product_id)

#     if not product:
#         return None

#     try:
#         for key, value in kwargs.items():
#             if hasattr(product, key):
#                 setattr(product, key, value)

#         session.commit()
#         session.refresh(product)
#         return product
#     except Exception:
#         session.rollback()
#         raise

# def delete_user(session, user_id):
#     user = session.get(User, user_id)

#     if not user:
#         return False

#     try:
#         session.delete(user)
#         session.commit()
#         return True
#     except Exception:
#         session.rollback()
#         raise

# def delete_product(session, product_id):
#     product = session.get(Product, product_id)

#     if not product:
#         return False

#     try:
#         session.delete(product)
#         session.commit()
#         return True
#     except Exception:
#         session.rollback()
#         raise
# user_manager.py
# import logging
# from sqlalchemy.exc import SQLAlchemyError
# from models import User, Base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# logging.basicConfig(level=logging.ERROR)

# engine = create_engine("sqlite:///store.db")
# SessionLocal = sessionmaker(bind=engine)

# try:
#     Base.metadata.create_all(engine)
# except SQLAlchemyError as e:
#     logging.error(e)

# class UserService:
#     def __init__(self, session):
#         self.session = session

#     def create_user(self, name, email, password_hash, phone, city):
#         try:
#             user = User(
#                 name=name,
#                 email=email,
#                 password_hash=password_hash,
#                 phone=phone,
#                 city=city
#             )
#             self.session.add(user)
#             self.session.commit()
#             self.session.refresh(user)
#             return user
#         except SQLAlchemyError as e:
#             self.session.rollback()
#             logging.error(e)
#             return None

#     def get_user(self, user_id):
#         try:
#             return self.session.get(User, user_id)
#         except SQLAlchemyError as e:
#             logging.error(e)
#             return None

#     def get_all_users(self):
#         try:
#             return self.session.query(User).all()
#         except SQLAlchemyError as e:
#             logging.error(e)
#             return []

#     def update_user(self, user_id, **kwargs):
#         try:
#             user = self.session.get(User, user_id)

#             if not user:
#                 return None

#             for key, value in kwargs.items():
#                 if hasattr(user, key):
#                     setattr(user, key, value)

#             self.session.commit()
#             self.session.refresh(user)
#             return user
#         except SQLAlchemyError as e:
#             self.session.rollback()
#             logging.error(e)
#             return None

#     def delete_user(self, user_id):
#         try:
#             user = self.session.get(User, user_id)

#             if not user:
#                 return False

#             self.session.delete(user)
#             self.session.commit()
#             return True
#         except SQLAlchemyError as e:
#             self.session.rollback()
#             logging.error(e)
#             return False

# def demo():
#     session = SessionLocal()

#     try:
#         service = UserService(session)

#         service.create_user(
#             "Rahul Sharma",
#             "rahul@gmail.com",
#             "hash123",
#             "9876543210",
#             "Indore"
#         )

#         service.create_user(
#             "Priya Verma",
#             "priya@gmail.com",
#             "hash456",
#             "9876543211",
#             "Bhopal"
#         )

#         service.create_user(
#             "Aman Patel",
#             "aman@gmail.com",
#             "hash789",
#             "9876543212",
#             "Mandsaur"
#         )

#         users = service.get_all_users()

#         for user in users:
#             print(user.id, user.name, user.email, user.city)

#         if users:
#             service.update_user(
#                 users[0].id,
#                 city="Ujjain"
#             )

#         if len(users) > 1:
#             service.delete_user(users[1].id)

#         print("Final Users")

#         users = service.get_all_users()

#         for user in users:
#             print(user.id, user.name, user.email, user.city)

#     except Exception as e:
#         session.rollback()
#         logging.error(e)
#     finally:
#         session.close()

# if __name__ == "__main__":
#     demo()


# #                                                       QUESTION  =2
# import logging
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from models import Base, User

# logging.basicConfig(level=logging.ERROR)

# engine = create_engine("sqlite:///store.db")
# SessionLocal = sessionmaker(bind=engine)

# try:
#     Base.metadata.create_all(engine)
# except Exception as e:
#     logging.error(e)


# class UserService:

#     def __init__(self, session):
#         self.session = session

#     def create_user(self, name, email, password_hash, phone, city):
#         try:
#             user = User(
#                 name=name,
#                 email=email,
#                 password_hash=password_hash,
#                 phone=phone,
#                 city=city
#             )

#             self.session.add(user)
#             self.session.commit()
#             self.session.refresh(user)

#             return user

#         except Exception as e:
#             self.session.rollback()
#             logging.error(e)
#             return None

#     def get_user(self, user_id):
#         try:
#             return self.session.get(User, user_id)

#         except Exception as e:
#             logging.error(e)
#             return None

#     def update_user(self, user_id, **kwargs):
#         try:
#             user = self.session.get(User, user_id)

#             if not user:
#                 return None

#             for key, value in kwargs.items():
#                 if hasattr(user, key):
#                     setattr(user, key, value)

#             self.session.commit()
#             self.session.refresh(user)

#             return user

#         except Exception as e:
#             self.session.rollback()
#             logging.error(e)
#             return None

#     def delete_user(self, user_id):
#         try:
#             user = self.session.get(User, user_id)

#             if not user:
#                 return False

#             self.session.delete(user)
#             self.session.commit()

#             return True

#         except Exception as e:
#             self.session.rollback()
#             logging.error(e)
#             return False


# def demo():
#     session = SessionLocal()

#     try:
#         service = UserService(session)

#         user1 = service.create_user(
#             "Rahul",
#             "rahul@gmail.com",
#             "hash123",
#             "9876543210",
#             "Indore"
#         )

#         user2 = service.create_user(
#             "Priya",
#             "priya@gmail.com",
#             "hash456",
#             "9876543211",
#             "Bhopal"
#         )

#         user3 = service.create_user(
#             "Aman",
#             "aman@gmail.com",
#             "hash789",
#             "9876543212",
#             "Ujjain"
#         )

#         users = session.query(User).all()

#         for user in users:
#             print(user.id, user.name, user.email, user.city)

#         if user1:
#             service.update_user(user1.id, city="Mandsaur")

#         if user2:
#             service.delete_user(user2.id)

#         print("Final Users")

#         users = session.query(User).all()

#         for user in users:
#             print(user.id, user.name, user.email, user.city)

#     except Exception as e:
#         session.rollback()
#         logging.error(e)

#     finally:
#         session.close()


# if __name__ == "__main__":
#     demo()
# # MODELS.PY M LIKHNE HTHE
# from sqlalchemy import create_engine, Integer, String
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# class Base(DeclarativeBase):
#     pass


# class User(Base):
#     __tablename__ = "users"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String(100), nullable=False)
#     email: Mapped[str] = mapped_column(String(150), nullable=False)
#     password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
#     phone: Mapped[str] = mapped_column(String(20))
#     city: Mapped[str] = mapped_column(String(100))                                                                                                                                











































































































































































































































































