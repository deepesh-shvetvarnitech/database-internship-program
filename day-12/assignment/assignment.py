#                                          operators
# price = 24
# qty = 3
# total = price*qty
# print(total)
# a = 10
# if a%2 ==0:
#     print("even")
# else:
#     print("odd")

# math = 80
# science = 75
# english = 90


# total = 240
# subjects = 3


# money = 1000
# spent = 350


# a = 17



# num = 25


# salary = 20000
# bonus = 5

# price = 120
# qty = 5




# price = 1000
# discount = 100



# marks = 65


# age = 20


# num = -5



# a = 27
# b = 4



# num = 21

# If num % 3 == 0
# print ("Divisible by 3")



# units = 50
# price_per_unit = 8



# bill = units * price_per_unit



# length = 10
# width = 5



# area = length * width



# length = 10
# width = 5
age = 44
if age >=40:
  print("eligibke")
else:
  print("not ligible")
price = 19.99
quantity = 3
sub_total = price * quantity
tax_rate = 0.12 
total = sub_total * (1 + tax_rate)
print(sub_total) 
print(total)    
age = 20
has_license = True

can_vote = age >= 18
can_drive = age >= 18 and has_license

if can_vote and can_drive:
    print("Person can vote and drive.")
elif can_vote or can_drive:
    print("Person can vote or drive.")
else:
   print("person can not vote or  drive")

income = 50000.0
expenses = 38000.0


savings = income - expenses
is_over_budget = expenses > income


print("Savings:", savings)


if is_over_budget:
    print("You are over budget.")
else:
    print("You are within budget.")

cart = ["laptop", "mouse", "keyboard"]


if "laptop" in cart:
    print("laptop found")
else:
    print("laptop not in cart")


if "monitor" in cart:
    print("monitor found")
else:
    print("monitor not in cart")

marks = 78


percentage = (marks / 100) * 100


if marks >= 90:
    grade = "A"
elif marks >= 70:
    grade = "B"
else:
    grade = "C"


print("Percentage:", percentage)
print("Grade:", grade)

count = 0


count += 1
count += 1
count += 1


count -= 1


print("Cart items:", count)




# num = 70


# balance = 5000
# withdraw = 1500


age = 25
has_membership = True


is_eligible = age >= 18 and has_membership


if is_eligible:
    print("Discount Eligible")
else:
    print("Discount Not Eligible")

salary = 40000
bonus = 5000


total_salary = salary + bonus


print("Total Salary:", total_salary)

temperature = 35


if temperature > 30:
    print("Hot")
else:
    print("Normal")

orders = ["phone", "charger", "headphones"]


if "phone" in orders:
    print("phone found")
else:
    print("phone not found")


if "laptop" in orders:
    print("laptop found")
else:
    print("laptop not found")

balance = 15000
withdrawal = 5000


if withdrawal <= balance:
    print("Withdrawal allowed")
else:
    print("Insufficient balance")

amount = 6000


if amount >= 5000:
    discount = amount * 0.10
    final_amount = amount - discount
else:
    final_amount = amount


print("Final Amount:", final_amount)

attendance = 85
medical_certificate = False


if attendance >= 75 or medical_certificate:
    print("Allowed")
else:
    print("Not Allowed")

items = 0


items += 1
items += 1
items += 1
items += 1


items -= 1


print("Items:", items)

number = 24


if number > 10 and number < 50:
    print("Number is in range")
else:
    print("Number is outside range")

username_correct = True
password_correct = True


if username_correct and password_correct:
    print("Login successful")
else:
    print("Login failed")

products = ["laptop", "mouse", "printer", "keyboard"]


if "printer" in products:
    print("printer is available")
else:
    print("printer is not available")


if "tablet" in products:
    print("tablet is available")
else:
    print("tablet is not available")

units = 250
rate = 8


bill = units * rate


if bill > 1500:
    print("High Bill")
else:
    print("Normal Bill")


print("Bill:", bill)

marks = 65
attendance = 80


if marks >= 40 and attendance >= 75:
    print("Pass")
else:
    print("Fail")

balance = 5000


balance += 1000
balance -= 1500


print("Final Balance:", balance)

order_amount = 1200
delivery_available = True


if order_amount >= 1000 and delivery_available:
    print("Free Delivery")
else:
    print("Delivery Charges Apply")

number = 27


if number % 2 == 0:
    print("Even")
else:
    print("Odd")

salary = 45000
years = 4


if salary < 50000 and years >= 3:
    print("Bonus Eligible")
else:
    print("Not Eligible")

marks1 = 85
marks2 = 75
marks3 = 90


total = marks1 + marks2 + marks3
average = total / 3


is_passed = average >= 40


if average >= 90:
    grade = "A"
elif average >= 70:
    grade = "B"
else:
    grade = "C"


print("Total:", total)
print("Average:", average)
print("Passed:", is_passed)
print("Grade:", grade)

sub_total = 5000
discount_rate = 0.10
tax_rate = 0.12


discounted = sub_total * (1 - discount_rate)
final_total = discounted * (1 + tax_rate)


shipping = 100
final_total += shipping


print("Subtotal:", sub_total)
print("Discounted Total:", discounted)
print("Final Total:", final_total)
units = 250
rate = 8


bill = units * rate


if units > 200:
    surcharge = bill * 0.05
else:
    surcharge = 0


final_bill = bill + surcharge


print("Bill:", bill)
print("Surcharge:", surcharge)
print("Final Bill:", final_bill)

basic_salary = 40000
bonus = 5000
tax_rate = 0.10


gross_salary = basic_salary + bonus
tax = gross_salary * tax_rate
net_salary = gross_salary - tax


print("Gross Salary:", gross_salary)
print("Tax:", tax)
print("Net Salary:", net_salary)

item1 = 1200
item2 = 800
item3 = 500


sub_total = item1 + item2 + item3


if sub_total >= 2000:
    discount = sub_total * 0.10
else:
    discount = 0


total = sub_total - discount


print("Subtotal:", sub_total)
print("Discount:", discount)
print("Final Total:", total)

balance = 25000
withdrawal = 8000


if withdrawal <= balance and withdrawal > 0:
    balance -= withdrawal
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Withdrawal Failed")

ticket_price = 250
tickets = 4


total = ticket_price * tickets


if tickets >= 4:
    discount = total * 0.10
else:
    discount = 0


final_amount = total - discount


print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)

recharge = 500
tax_rate = 0.18


tax = recharge * tax_rate
final_amount = recharge + tax


if final_amount >= 500:
    print("Premium Recharge")
else:
    print("Regular Recharge")


print("Tax:", tax)
print("Final Amount:", final_amount)

marks = 85
attendance = 90


if marks >= 80 and attendance >= 75:
    scholarship = True
else:
    scholarship = False


print("Scholarship Eligible:", scholarship)

food_bill = 1800
tax_rate = 0.05
service_charge = 100


tax = food_bill * tax_rate
total = food_bill + tax
total += service_charge


print("Food Bill:", food_bill)
print("Tax:", tax)
print("Service Charge:", service_charge)
print("Final Bill:", total)

order_amount = 1500
delivery_available = True


if order_amount >= 1000 and delivery_available:
    delivery_charge = 0
else:
    delivery_charge = 100


final_amount = order_amount + delivery_charge


print("Delivery Charge:", delivery_charge)
print("Final Amount:", final_amount)

monthly_fee = 1000
months = 6


total = monthly_fee * months


if months >= 6:
    discount = total * 0.15
else:
    discount = 0


final_amount = total - discount


print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)

room_price = 3000
nights = 4
tax_rate = 0.12


room_total = room_price * nights
tax = room_total * tax_rate
final_bill = room_total + tax


print("Room Total:", room_total)
print("Tax:", tax)
print("Final Bill:", final_bill)

marks1 = 75
marks2 = 82
marks3 = 68
attendance = 80


total = marks1 + marks2 + marks3
average = total / 3


if average >= 40 and attendance >= 75:
    result = "Pass"
else:
    result = "Fail"


print("Total:", total)
print("Average:", average)
print("Result:", result)

sub_total = 4000
coupon = "SAVE10"


if coupon == "SAVE10" and sub_total >= 3000:
    discount = sub_total * 0.10
else:
    discount = 0


final_total = sub_total - discount


print("Discount:", discount)
print("Final Total:", final_total)

balance = 20000
deposit = 5000
withdrawal = 7000


balance += deposit
balance -= withdrawal


if balance >= 0:
    print("Transaction Successful")
else:
    print("Insufficient Balance")


print("Final Balance:", balance)

units = 350


if units <= 100:
    category = "Low Usage"
elif units <= 300:
    category = "Medium Usage"
else:
    category = "High Usage"


print("Units:", units)
print("Category:", category)

#                                             LIST STRING DIC 
cart = []


cart.append("laptop")
cart.append("mouse")
cart.append("keyboard")


for item in cart:
    print(item)


item_count = len(cart)


print("Total Items:", item_count)

user = {
    "name": "Alice",
    "age": 25,
    "city": "Mumbai"
}


user["email"] = "alice@gmail.com"
user["city"] = "Delhi"


for key in user:
    print(key + ":", user[key])


print("Phone:", user.get("phone", "Not provided"))

students = []


students.append({"name": "Rahul", "marks": 85})
students.append({"name": "Priya", "marks": 72})


total = 0


for student in students:
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    total += student["marks"]


average = total / len(students)


print("Average Marks:", average)

log_line = "2024-05-24 INFO User login successful"


parts = log_line.split()


level = parts[1]
message = " ".join(parts[2:])


print("Level:", level)
print("Message:", message)

products = []


products.append({
    "id": 1,
    "name": "Laptop",
    "price": 50000
})


products.append({
    "id": 2,
    "name": "Phone",
    "price": 25000
})


for product in products:
    print(product["name"], product["price"])


print("Products under 30000:")


for product in products:
    if product["price"] < 30000:
        print(product["name"], product["price"])

name = input("Name: ").strip()
email = input("Email: ").strip()


if name != "" and "@" in email:
    user = {
        "name": name,
        "email": email
    }


    print(user)
else:
    print("Invalid input")

accounts = []


accounts.append({
    "acc_no": 101,
    "name": "Alice",
    "balance": 5000
})


accounts.append({
    "acc_no": 102,
    "name": "Rahul",
    "balance": 8000
})


accounts.append({
    "acc_no": 103,
    "name": "Priya",
    "balance": 12000
})


for account in accounts:
    print(account)


search_acc = int(input("Enter Account Number: "))


for account in accounts:
    if account["acc_no"] == search_acc:
        print("Account Found:", account)
        break
else:
    print("Account Not Found")

grocery = []


grocery.append("rice")
grocery.append("milk")
grocery.append("bread")
grocery.append("eggs")


for item in grocery:
    print(item)


print("Total Items:", len(grocery))


if "milk" in grocery:
    print("Milk is available")
else:
    print("Milk is not available")

employees = []


employees.append({"id": 101, "name": "Amit", "salary": 30000})
employees.append({"id": 102, "name": "Neha", "salary": 40000})
employees.append({"id": 103, "name": "Ravi", "salary": 35000})


total_salary = 0


for employee in employees:
    print(employee["name"], employee["salary"])
    total_salary += employee["salary"]


print("Total Salary:", total_salary)

contacts = {
    "Amit": "9876543210",
    "Neha": "9876501234"
}


contacts["Ravi"] = "9876511111"
contacts["Neha"] = "9999999999"


print(contacts.get("Amit", "Contact Not Found"))
print(contacts.get("Rahul", "Contact Not Found"))


for name in contacts:
    print(name, ":", contacts[name])

expenses = []


expenses.append({"category": "Food", "amount": 500})
expenses.append({"category": "Travel", "amount": 800})
expenses.append({"category": "Shopping", "amount": 1200})


total = 0


for expense in expenses:
    print(expense["category"], expense["amount"])
    total += expense["amount"]


print("Total Expense:", total)


for expense in expenses:
    if expense["amount"] > 700:
        print("High Expense:", expense["category"])

users = {
    "admin": "1234",
    "rahul": "pass123"
}


username = input("Username: ")
password = input("Password: ")


stored_password = users.get(username)


if stored_password == password:
    print("Login Successful")
else:
    print("Invalid Login")

students = []


students.append({"roll": 1, "name": "Rahul", "marks": 85})
students.append({"roll": 2, "name": "Priya", "marks": 92})
students.append({"roll": 3, "name": "Aman", "marks": 76})


roll = int(input("Enter Roll Number: "))


for student in students:
    if student["roll"] == roll:
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        break
else:
    print("Student Not Found")

products = []


products.append({"id": 1, "name": "Laptop", "price": 50000})
products.append({"id": 2, "name": "Mouse", "price": 800})
products.append({"id": 3, "name": "Keyboard", "price": 1500})


search = input("Enter Product Name: ")


for product in products:
    if product["name"].lower() == search.lower():
        print("Name:", product["name"])
        print("Price:", product["price"])
        break
else:
    print("Product Not Found")

orders = []


orders.append({"order_id": 101, "customer": "Amit", "amount": 1500})
orders.append({"order_id": 102, "customer": "Rahul", "amount": 2500})
orders.append({"order_id": 103, "customer": "Priya", "amount": 1000})


total = 0


for order in orders:
    print(order)
    total += order["amount"]


print("Total Order Amount:", total)
print("Number of Orders:", len(orders))

name = input("Name: ").strip()
email = input("Email: ").strip()


if name != "" and "@" in email and "." in email:
    user = {
        "name": name,
        "email": email
    }


    print(user)
else:
    print("Invalid Input")

log = "2026-08-14 ERROR Database connection failed"


parts = log.split()


date = parts[0]
level = parts[1]
message = " ".join(parts[2:])


print("Date:", date)
print("Level:", level)
print("Message:", message)

attendance = []


attendance.append({"name": "Rahul", "present": True})
attendance.append({"name": "Priya", "present": False})
attendance.append({"name": "Aman", "present": True})


present_count = 0


for student in attendance:
    print(student["name"], student["present"])


    if student["present"]:
        present_count += 1


print("Present Students:", present_count)

movies = []


movies.append("Avatar")
movies.append("Titanic")
movies.append("Inception")
movies.append("Interstellar")


for movie in movies:
    print(movie)


print("Total Movies:", len(movies))


if "Inception" in movies:
    print("Inception Found")
else:
    print("Inception Not Found")


search = input("Enter Movie Name: ")


if search in movies:
    print("Movie Found")
else:
    print("Movie Not Found")

accounts = []


accounts.append({"acc_no": 101, "name": "Amit", "balance": 5000})
accounts.append({"acc_no": 102, "name": "Rahul", "balance": 8000})
accounts.append({"acc_no": 103, "name": "Priya", "balance": 12000})


acc_no = int(input("Enter Account Number: "))


for account in accounts:
    if account["acc_no"] == acc_no:
        print(account)
        break
else:
    print("Account Not Found")

feedback = []


feedback.append({
    "name": "Amit",
    "rating": 5,
    "comment": "Excellent"
})


feedback.append({
    "name": "Rahul",
    "rating": 4,
    "comment": "Good"
})


feedback.append({
    "name": "Priya",
    "rating": 5,
    "comment": "Very Good"
})


total_rating = 0


for item in feedback:
    print(item["name"], item["rating"])
    total_rating += item["rating"]


average = total_rating / len(feedback)


print("Average Rating:", average)


for item in feedback:
    if item["rating"] == 5:
        print("5-Star Customer:", item["name"])

inventory = []


inventory.append({"name": "Laptop", "quantity": 3, "price": 50000})
inventory.append({"name": "Mouse", "quantity": 10, "price": 800})
inventory.append({"name": "Keyboard", "quantity": 4, "price": 1500})


total_value = 0


for product in inventory:
    print(product)


    value = product["quantity"] * product["price"]
    total_value += value


    if product["quantity"] < 5:
        print("Low Stock:", product["name"])


print("Total Inventory Value:", total_value)

courses = []


courses.append({"name": "Python", "students": 30})
courses.append({"name": "SQL", "students": 25})
courses.append({"name": "Java", "students": 20})


total_students = 0


for course in courses:
    print(course["name"], course["students"])
    total_students += course["students"]


print("Total Students:", total_students)


for course in courses:
    if course["name"] == "Python":
        print("Python Course:", course)

orders = []


orders.append({
    "order_id": 101,
    "customer": "Amit",
    "food": "Pizza",
    "amount": 600
})


orders.append({
    "order_id": 102,
    "customer": "Rahul",
    "food": "Burger",
    "amount": 400
})


orders.append({
    "order_id": 103,
    "customer": "Priya",
    "food": "Biryani",
    "amount": 800
})


total = 0


for order in orders:
    print(order)
    total += order["amount"]


print("Total Amount:", total)


for order in orders:
    if order["amount"] > 500:
        print("Order above 500:", order)


search_id = int(input("Enter Order ID: "))


for order in orders:
    if order["order_id"] == search_id:
        print("Order Found:", order)
        break
else:
    print("Order Not Found")

name = input("Name: ").strip()
age = int(input("Age: "))
email = input("Email: ").strip()


if name != "" and age >= 18 and "@" in email:
    user = {
        "name": name,
        "age": age,
        "email": email
    }


    print("Registration Successful")
    print(user)
else:
    print("Invalid Registration")  

cart_items = []


products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 499}
]


cart_items.append({"id": 1, "quantity": 1})
cart_items.append({"id": 2, "quantity": 2})


subtotal = 0


for cart_item in cart_items:
    for product in products:
        if cart_item["id"] == product["id"]:
            name = product["name"]
            price = product["price"]
            quantity = cart_item["quantity"]
            total = price * quantity


            subtotal += total


            print("Item:", name)
            print("Quantity:", quantity)
            print("Price:", price)
            print("Total:", total)
            print()


if subtotal > 50000:
    discount = subtotal * 0.10
else:
    discount = 0


final_total = subtotal - discount


print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Total:", final_total)

students = []


students.append({
    "roll": 1,
    "name": "Rahul",
    "marks": [75, 80, 90]
})


students.append({
    "roll": 2,
    "name": "Priya",
    "marks": [60, 70, 65]
})


students.append({
    "roll": 3,
    "name": "Aman",
    "marks": [45, 55, 50]
})


students.append({
    "roll": 4,
    "name": "Neha",
    "marks": [35, 40, 30]
})


for student in students:
    total = 0


    for mark in student["marks"]:
        total += mark


    average = total / len(student["marks"])


    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"


    print("Roll:", student["roll"])
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("Total:", total)
    print("Average:", average)
    print("Result:", result)
    print("--------------------")  


#                                              OOPS
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"




user1 = User("Rahul", "rahul@gmail.com")


print(user1)

class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")




account = BankAccount("Rahul", 101, 5000)


account.deposit(2000)
account.withdraw(3000)


print("Balance:", account.balance)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price




class Cart:
    def __init__(self):
        self.items = []


    def add_item(self, product, qty):
        self.items.append({
            "product": product,
            "quantity": qty
        })


    def show_cart(self):
        for item in self.items:
            product = item["product"]
            qty = item["quantity"]


            print("Name:", product.name)
            print("Price:", product.price)
            print("Quantity:", qty)
            print("Total:", product.price * qty)
            print()




laptop = Product("Laptop", 50000)
mouse = Product("Mouse", 500)


cart = Cart()


cart.add_item(laptop, 1)
cart.add_item(mouse, 2)


cart.show_cart()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"




class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size


    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}, Team Size: {self.team_size}"




manager = Manager("Amit", 60000, 10)


print(manager)

class Shape:
    def area(self):
        pass




class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius * self.radius




class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height




shapes = [
    Circle(5),
    Rectangle(10, 5),
    Circle(3)
]


for shape in shapes:
    print("Area:", shape.area())

class Bank:
    def __init__(self, balance):
        self._balance = balance


    @property
    def balance(self):
        return self._balance


    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative")




bank = Bank(5000)


print("Balance:", bank.balance)


bank.balance = 8000


print("Updated Balance:", bank.balance)
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks


    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)




s1 = Student("Rahul", 1, 85)
s2 = Student("Priya", 2, 92)


s1.display()
s2.display()


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def discount(self):
        return self.price * 0.90




product = Product("Laptop", 50000)


print("Product:", product.name)
print("Original Price:", product.price)
print("Final Price:", product.discount())

class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed


    def accelerate(self):
        self.speed += 20


    def brake(self):
        self.speed -= 10




car = Car("Toyota", "Fortuner", 60)


car.accelerate()
print("Speed:", car.speed)


car.brake()
print("Speed:", car.speed)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100




employee = Employee("Amit", 40000)


employee.increase_salary(10)


print("Name:", employee.name)
print("Salary:", employee.salary)


class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")




account = BankAccount("Rahul", 10000)


account.deposit(5000)
account.withdraw(3000)


print("Holder:", account.holder)
print("Balance:", account.balance)


class Vehicle:
    def __init__(self, brand):
        self.brand = brand




class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model




car = Car("Toyota", "Fortuner")


print("Brand:", car.brand)
print("Model:", car.model)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary




class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department




manager = Manager("Neha", 70000, "IT")


print("Name:", manager.name)
print("Salary:", manager.salary)
print("Department:", manager.department)


class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")




class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")




payments = [
    CreditCard(),
    UPI()
]


for payment in payments:
    payment.pay(1000)


class Dog:
    def sound(self):
        print("Dog says Woof")




class Cat:
    def sound(self):
        print("Cat says Meow")




animals = [
    Dog(),
    Cat()
]


for animal in animals:
    animal.sound()

class Person:
    def __init__(self, age):
        self._age = age


    @property
    def age(self):
        return self._age


    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Invalid Age")




person = Person(20)


print(person.age)


person.age = 25


print(person.age)


person.age = -5


class ShoppingCart:
    def __init__(self):
        self.items = []


    def add_item(self, name, price, quantity):
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })


    def calculate_total(self):
        total = 0


        for item in self.items:
            total += item["price"] * item["quantity"]


        return total




cart = ShoppingCart()


cart.add_item("Laptop", 50000, 1)
cart.add_item("Mouse", 500, 2)
cart.add_item("Keyboard", 1500, 1)


print("Total:", cart.calculate_total())

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def total_marks(self):
        return sum(self.marks)


    def average(self):
        return self.total_marks() / len(self.marks)


    def result(self):
        if self.average() >= 40:
            return "Pass"
        else:
            return "Fail"




student = Student("Rahul", [75, 80, 65])


print("Name:", student.name)
print("Total:", student.total_marks())
print("Average:", student.average())
print("Result:", student.result())




class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True


    def borrow(self):
        if self.is_available:
            self.is_available = False
            print("Book Borrowed")
        else:
            print("Book Not Available")


    def return_book(self):
        self.is_available = True
        print("Book Returned")




book = Book("Python Basics", "Rahul")


book.borrow()
book.borrow()
book.return_book()
book.borrow()

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


    def display(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone:", self.phone)
        print()




customers = [
    Customer("Amit", "amit@gmail.com", "9876543210"),
    Customer("Rahul", "rahul@gmail.com", "9876543211"),
    Customer("Priya", "priya@gmail.com", "9876543212")
]


for customer in customers:
    customer.display()
