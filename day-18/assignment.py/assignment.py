'''import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

print("Host:", db_host)
print("Port:", db_port)
print("Database:", db_name)
print("User:", db_user)'''

'''import os
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv("DB_NAME")

print("Database:", db_name)'''

'''import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")

print("Host:", db_host)
print("Port:", db_port)
print("Database:", db_name)
print("User:", db_user)
'''
'''import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

safe_string = f"postgresql://{db_user}:****@{db_host}:{db_port}/{db_name}"

print("Connection String:", safe_string)
'''
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

required_vars = [
    db_host,
    db_port,
    db_name,
    db_user,
    db_password
]

if all(required_vars):
    print("Database configuration is valid")
    print("Database:", db_name)
else:
    print("Missing database configuration")

