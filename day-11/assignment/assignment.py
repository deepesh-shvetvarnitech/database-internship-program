#                                                 conditional statment
num =  7
if num > 0 :
    print('positbe')
elif num < 0:
    print("negative")
else  :
    print("zero")

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

age = int(input("Enter your age: "))

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")

    num = int(input("Enter a number: "))

if num % 5 == 0 and num % 10 == 0:
    print("Divisible by both 5 and 10")
else:
    print("Not divisible by both")

num = int(input("Enter a number: "))

if num % 5 == 0 or num % 10 == 0:
    print("Divisible by 5 or 10")
else:
    print("Not divisible by 5 or 10")

password = input("Enter your password: ")

if len(password) >= 8:
    print("Valid Password")
else:
    print("Password is too short")


marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail") 

marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

temp = int(input("Enter temperature: "))

if temp < 20:
    print("Cold")
elif temp <= 30:
    print("Normal")
else:
    print("Hot")
    balance = int(input("Enter balance: "))

if balance == 0:
    print("No Balance")
elif balance < 1000:
    print("Low Balance")
elif balance < 10000:
    print("Normal Balance")
else:
    print("High Balance")


balance = 10000
amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid Amount")
elif amount > balance:
    print("Insufficient Balance")
else:
    print("Withdrawal Successful")

amount = int(input("Enter deposit amount: "))

if amount <= 0:
    print("Invalid Deposit")
elif amount <= 10000:
    print("Normal Deposit")
else:
    print("Large Deposit")

pin = int(input("Enter PIN: "))

if pin == 1234:
    print("Access Granted")
else:
    print("Access Denied")


username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
elif username != "admin":
    print("Wrong Username")
else:
    print("Wrong Password")


balance = int(input("Enter balance: "))

if balance < 1000:
    print("Minimum Balance Not Maintained")
else:
    print("Account Active")

balance = 15000
amount = int(input("Enter transfer amount: "))

if amount <= 0:
    print("Invalid Amount")
elif amount <= balance:
    print("Transfer Successful")
else:
    print("Insufficient Balance")

balance = 5000
deposit = int(input("Enter deposit amount: "))

balance = balance + deposit

if deposit >= 10000:
    balance = balance + 500
    print("Bonus Added")

print("Final Balance:", balance)

marks = int(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
else:
    grade = "C"

if marks >= 40:
    result = "Pass"
else:
    result = "Fail"

print("Grade:", grade)
print("Result:", result)

salary = float(input("Enter salary: "))

if salary >= 80000:
    category = "High Salary"
elif salary >= 50000:
    category = "Good Salary"
elif salary >= 30000:
    category = "Average Salary"
else:
    category = "Low Salary"

if salary >= 50000:
    bonus_rate = 10
else:
    bonus_rate = 5

bonus = salary * bonus_rate / 100
final_salary = salary + bonus

print("Salary Category:", category)
print("Bonus:", bonus)
print("Final Salary:", final_salary)

#                                                      loop 
for i in range(1, 6):
    print(i)
fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)
    for i in range(1, 21):
       if i % 2 == 0:
        print(i)


total = 0

for i in range(1, 6):
    print(i)
    total = total + i

print("Sum =", total)

cart = ["book", "pen", "notebook"]

for item in cart:
    print(item)

for i, item in enumerate(cart):
    print(i, item)

name = "Alice"

for letter in name:
    print(letter)

for letter in name:
    if letter in "aeiou":
        print(letter)

while True:
    value = input("Enter something: ")

    if value == "stop":
        break

    print(value)

for i in range(1, 11):
    if i == 6:
        break

    if i % 2 == 0:
        continue

    print(i)

marks = [75, 88, 92, 60, 77]

total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)

print("Total =", total)
print("Average =", average)

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} × {j} = {i * j}")
    print()   

total = 0

for i in range(1, 11):
    print(i)
    total = total + i

print("Sum =", total)





items = ["milk", "bread", "eggs", "rice"]

for item in items:
    print(item)

for i, item in enumerate(items):
    print(i, item)


word = "Programming"

for letter in word:
    print(letter)

for letter in word:
    if letter.lower() not in "aeiou":
        print(letter)

while True:
    password = input("Enter password: ")

    if password == "python123":
        print("Access Granted")
        break

    print("Wrong Password")


for i in range(1, 21):
    if i == 12:
        break

    print(i)

for i in range(1, 16):
    if i % 3 == 0:
        continue

    print(i)


marks = [65, 78, 89, 92, 55]

total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)

print("Total =", total)
print("Average =", average)


numbers = [25, 67, 12, 89, 45, 34]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest =", largest)

numbers = [45, 12, 78, 23, 9, 56]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest =", smallest)


numbers = [10, 15, 22, 31, 44, 57, 60]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even =", even)
print("Odd =", odd)


num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "×", i, "=", num * i)


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")

    print()

prices = [100, 250, 75, 300, 150]

total = 0

for price in prices:
    total = total + price

print("Total =", total)


numbers = [10, -5, 20, -8, 15, -2, 30]

positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += 1
    else:
        negative += 1

print("Positive =", positive)
print("Negative =", negative)


cart = ["book", "pen", "laptop", "mouse"]

found = False

for item in cart:
    if item == "laptop":
        found = True
        break

if found:
    print("Item Found")
else:
    print("Item Not Found")

students = ["Alice", "Bob", "Charlie"]
marks_lists = [[75, 80, 90], [45, 50, 55], [88, 92, 95]]

for i in range(len(students)):
    total = 0

    for mark in marks_lists[i]:
        total = total + mark

    average = total / len(marks_lists[i])

    print("Student:", students[i])
    print("Average:", average)

    if average >= 50:
        print("Pass")
    else:
        print("Fail")

    print()

students = ["Alice", "Bob", "Charlie"]
marks_lists = [[75, 80, 90], [45, 50, 55], [88, 92, 95]]

for i in range(len(students)):
    total = 0

    for mark in marks_lists[i]:
        total = total + mark

    average = total / len(marks_lists[i])

    print("Student:", students[i])
    print("Average:", average)

    if average >= 50:
        print("Pass")
    else:
        print("Fail")

    print()

cart_items = [
    ("Laptop", 49999),
    ("Mouse", 499),
    ("Keyboard", 1499)
]

subtotal = 0

for item, price in cart_items:
    subtotal = subtotal + price
    print("Item:", item)
    print("Price:", price)
    print("Running Total:", subtotal)
    print()

if subtotal > 50000:
    discount = subtotal * 0.10
else:
    discount = 0

final_total = subtotal - discount

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Total:", final_total)  

transactions = [500, -200, 1000, -300]

balance = 0

for transaction in transactions:
    balance = balance + transaction
    print("Transaction:", transaction)
    print("Balance:", balance)

print("Final Balance:", balance)

salaries = [25000, 40000, 55000, 30000, 70000]

total = 0
count = 0

for salary in salaries:
    total = total + salary

    if salary > 40000:
        count = count + 1

average = total / len(salaries)

print("Total Salary:", total)
print("Average Salary:", average)
print("Above 40000:", count)

items = [
    ("Rice", 500),
    ("Milk", 60),
    ("Bread", 40),
    ("Oil", 150)
]

subtotal = 0

for item, price in items:
    subtotal = subtotal + price
    print(item, price)

if subtotal > 500:
    discount = subtotal * 0.05
else:
    discount = 0

final_bill = subtotal - discount

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Bill:", final_bill)


attendance = ["P", "P", "A", "P", "A", "P", "P"]

present = 0
absent = 0

for status in attendance:
    if status == "P":
        present += 1
    else:
        absent += 1

percentage = (present / len(attendance)) * 100

print("Present:", present)
print("Absent:", absent)
print("Attendance:", percentage, "%")

if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

transactions = [1000, -300, -200, 500, -100]

balance = 5000

for transaction in transactions:
    balance = balance + transaction

    if balance < 0:
        break

    print("Transaction:", transaction)
    print("Balance:", balance)

print("Final Balance:", balance)

students = {
    "Alice": [80, 75, 90],
    "Bob": [45, 50, 40],
    "Charlie": [90, 95, 88]
}

for name, marks in students.items():
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    print("Name:", name)
    print("Total:", total)
    print("Average:", average)

    if average >= 50:
        print("Pass")
    else:
        print("Fail")

    print()


products = [
    ("Laptop", 5),
    ("Mouse", 0),
    ("Keyboard", 8),
    ("Monitor", 0)
]

out_of_stock = 0

for product, stock in products:
    print("Product:", product)
    print("Stock:", stock)

    if stock > 0:
        print("In Stock")
    else:
        print("Out of Stock")
        out_of_stock += 1

    print()

print("Out of Stock Products:", out_of_stock)


orders = [
    ("Pizza", 250),
    ("Burger", 150),
    ("Coke", 50),
    ("Fries", 100)
]

total = 0

for item, price in orders:
    total += price
    print(item, price)

if total > 500:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)

numbers = [12, 7, 25, 30, 41, 18, 9]

even = 0
odd = 0
total = 0
largest = numbers[0]

for num in numbers:
    total += num

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    if num > largest:
        largest = num

print("Even:", even)
print("Odd:", odd)
print("Sum:", total)
print("Largest:", largest)


correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    attempts += 1

    if password == correct_password:
        print("Login Successful")
        break

    print("Wrong Password")

if attempts == 3 and password != correct_password:
    print("Account Locked")


for row in range(1, 4):
    for seat in range(1, 5):
        print("Row", row, "Seat", seat)



sales = [1200, 2500, 800, 3000, 1500]

total = 0
above_2000 = 0

for sale in sales:
    total += sale

    if sale > 2000:
        above_2000 += 1

average = total / len(sales)

print("Total Sales:", total)
print("Average Sales:", average)
print("Sales Above 2000:", above_2000)

def add(a, b):
    return a + b


def greet(name):
    message = "Hello " + name
    return message



def add(a, b):
    return a + b

result = add(5, 3)

print(result)






def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)


None


def add(a, b):
    return a + b

result = add(10, 20)

print(result)


def add(a, b):
    return a + b

x = add(10, 20)
y = add(50, 30)

total = x + y

print(total)

total = 0

for i in range(1, 6):
    print(i)
    total = total + i

print("Sum =", total)

cart = ["book", "pen", "notebook"]

for item in cart:
    print(item)

print("With Index:")

for i, item in enumerate(cart):
    print(i, item)


name = "Alice"

for letter in name:
    print(letter)

print("Vowels:")

for letter in name:
    if letter in "aeiou":
        print(letter)

while True:
    value = input("Enter something: ")

    if value == "stop":
        break

    print("You entered:", value)

students = ["Alice", "Bob", "Charlie"]

marks_lists = [
    [75, 80, 90],
    [45, 50, 55],
    [88, 92, 95]
]

for i in range(len(students)):

    total = 0

    for mark in marks_lists[i]:
        total = total + mark

    average = total / len(marks_lists[i])

    print("Student:", students[i])
    print("Average:", average)

    if average >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

    print()


for i in range(len(students)):

  for mark in marks_lists[i]:



   total = total + mark



if average >= 50:


  cart_items = [
    ("Laptop", 49999),
    ("Mouse", 499),
    ("Keyboard", 1499)
]

subtotal = 0

for item, price in cart_items:

    subtotal = subtotal + price

    print("Item:", item)
    print("Price:", price)
    print("Running Total:", subtotal)
    print()

if subtotal > 50000:
    discount = subtotal * 0.10
else:
    discount = 0

final_price = subtotal - discount

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Price:", final_price) 

students = ["Rahul", "Aman", "Priya"]

attendance = [
    [22, 25, 24],
    [18, 20, 19],
    [28, 27, 29]
]

for i in range(len(students)):

    total = 0

    for days in attendance[i]:
        total = total + days

    average = total / len(attendance[i])

    print("Student:", students[i])
    print("Total:", total)
    print("Average:", average)

    if average >= 75:
        print("Result: Eligible")
    else:
        print("Result: Not Eligible")

    print()

orders = [
    ("Pizza", 350),
    ("Burger", 200),
    ("Fries", 120),
    ("Coke", 80)
]

subtotal = 0

for item, price in orders:

    subtotal = subtotal + price

    print("Item:", item)
    print("Price:", price)
    print("Running Total:", subtotal)
    print()

if subtotal > 600:
    discount = subtotal * 0.15
else:
    discount = 0

final_bill = subtotal - discount

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Bill:", final_bill)


products = [
    ("Laptop", 5),
    ("Mouse", 0),
    ("Keyboard", 12),
    ("Monitor", 0),
    ("Printer", 7)
]

out_of_stock = 0

for product, stock in products:

    print("Product:", product)
    print("Stock:", stock)

    if stock > 0:
        print("Status: In Stock")
    else:
        print("Status: Out of Stock")
        out_of_stock += 1

    print()

print("Total Out of Stock:", out_of_stock)


transactions = [1000, -500, 2000, -300, -700]

balance = 5000

for transaction in transactions:

    balance = balance + transaction

    print("Transaction:", transaction)
    print("Running Balance:", balance)
    print()

print("Final Balance:", balance)

sales = [
    ("Rahul", 50000),
    ("Aman", 35000),
    ("Priya", 65000),
    ("Neha", 45000)
]

total = 0
above_50000 = 0

for name, amount in sales:

    total = total + amount

    print("Salesperson:", name)
    print("Sales:", amount)

    if amount > 50000:
        above_50000 += 1

    print()

average = total / len(sales)

print("Total Sales:", total)
print("Average Sales:", average)
print("Above 50000:", above_50000)


movies = [
    ("Avatar", 8.5),
    ("Inception", 9.0),
    ("Titanic", 7.8),
    ("Joker", 8.8)
]

total = 0
highly_rated = 0

for movie, rating in movies:

    total = total + rating

    print("Movie:", movie)
    print("Rating:", rating)

    if rating >= 8.5:
        print("Highly Rated")
        highly_rated += 1
    else:
        print("Normal")

    print()

average = total / len(movies)

print("Average Rating:", average)
print("Highly Rated Movies:", highly_rated)


orders = [
    ("Order1", 1200),
    ("Order2", 700),
    ("Order3", 2500),
    ("Order4", 400)
]

total = 0

for order, amount in orders:

    if amount >= 1000:
        delivery = 0
    else:
        delivery = 100

    payable = amount + delivery
    total = total + payable

    print("Order:", order)
    print("Amount:", amount)
    print("Delivery:", delivery)
    print("Payable:", payable)
    print()

print("Total Payable:", total)

members = [
    ("Alice", 2),
    ("Bob", 7),
    ("Charlie", 0),
    ("David", 10)
]

total_fine = 0

for name, days in members:

    if days > 5:
        fine = (days - 5) * 10
    else:
        fine = 0

    total_fine = total_fine + fine

    print("Member:", name)
    print("Overdue Days:", days)
    print("Fine:", fine)
    print()

print("Total Fine:", total_fine)



#                                          FUNTIONS
def greet(name):
    print(f"Hello, {name}")

greet("Alice")


def greet(name="Guest"):
    print(f"Hello, {name}")

greet()

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


result = multiply(add(2, 3), 2)

print(result)


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


greet("Alice")
greet("Bob", "Hi")


def calc_total(items, discount=0):
    subtotal = sum(items)
    discount_amount = subtotal * discount / 100
    final_total = subtotal - discount_amount

    return subtotal, discount_amount, final_total


items = [100, 200, 300]

subtotal, discount_amount, final_total = calc_total(items, 10)

print("Subtotal:", subtotal)
print("Discount:", discount_amount)
print("Final Total:", final_total)


def compute_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 70:
        return "B"
    else:
        return "C"


marks = 85

grade = compute_grade(marks)

print("Marks:", marks)
print("Grade:", grade)


def is_valid_email(email):
    if email != "" and "@" in email:
        return True
    else:
        return False


print(is_valid_email("alice@example.com"))
print(is_valid_email(""))


def calculate_area(length, width):
    return length * width


area = calculate_area(10, 5)

print("Area:", area)

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


result = check_even_odd(25)

print(result)


def calculate_discount(price, discount=10):
    discount_amount = price * discount / 100
    final_price = price - discount_amount

    return final_price


result = calculate_discount(1000, 20)

print("Final Price:", result)

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


result = find_max(25, 60, 40)

print("Largest:", result)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


temperature = celsius_to_fahrenheit(25)

print("Fahrenheit:", temperature)


def cart_total(prices):
    return sum(prices)


prices = [100, 250, 150, 500]

total = cart_total(prices)

print("Total:", total)


def check_password(password):
    if len(password) >= 8:
        return "Valid"
    else:
        return "Invalid"


result = check_password("python123")

print(result)

def calculate_salary(basic, bonus=5000):
    return basic + bonus


salary = calculate_salary(30000)

print("Total Salary:", salary)


def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)

    return average


numbers = [80, 90, 70, 60]

result = calculate_average(numbers)

print("Average:", result)

def login(username, password):
    if username == "admin" and password == "12345":
        return "Login Successful"
    else:
        return "Invalid Login"


result = login("admin", "12345")

print(result)


def check_result(marks, passing_marks=50):
    if marks >= passing_marks:
        return "Pass"
    else:
        return "Fail"


result = check_result(65)

print(result)


def calculate_bill(price, quantity, tax=0.05):
    subtotal = price * quantity
    final_bill = subtotal + (subtotal * tax)

    return final_bill


bill = calculate_bill(500, 3)

print("Final Bill:", bill)

def get_length(text):
    return len(text)


result = get_length("Python Programming")

print("Length:", result)

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


interest = simple_interest(10000, 5, 2)

print("Simple Interest:", interest)

def check_order_status(status="Pending"):
    if status == "Pending":
        return "Order is Pending"
    elif status == "Shipped":
        return "Order is Shipped"
    elif status == "Delivered":
        return "Order is Delivered"
    else:
        return "Unknown Status"


print(check_order_status())


prices = [100, 200, 150]


def calc_subtotal(prices):
    return sum(prices)


def calc_discounted_total(prices, discount=10):
    subtotal = calc_subtotal(prices)
    discount_amount = subtotal * discount / 100
    final_total = subtotal - discount_amount

    return discount_amount, final_total


def print_invoice(prices, discount=10):
    subtotal = calc_subtotal(prices)

    discount_amount, final_total = calc_discounted_total(
        prices, discount
    )

    print("Subtotal:", subtotal)
    print("Discount amount:", discount_amount)
    print("Final total:", final_total)


print_invoice(prices)


student = {
    "name": "Rahul",
    "marks": [75, 80, 90]
}


def calc_avg_marks(marks):
    return sum(marks) / len(marks)


def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"


def generate_report(student):
    avg = calc_avg_marks(student["marks"])
    grade = get_grade(avg)

    return {
        "name": student["name"],
        "avg": avg,
        "grade": grade
    }


report = generate_report(student)

print(report)
