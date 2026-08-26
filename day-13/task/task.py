employees = [
    {"id": 101, "name": "Rahul", "department": "IT", "days_present": 22, "daily_salary": 1200},
    {"id": 102, "name": "Priya", "department": "HR", "days_present": 19, "daily_salary": 1000},
    {"id": 103, "name": "Amit", "department": "IT", "days_present": 25, "daily_salary": 1500},
    {"id": 104, "name": "Neha", "department": "Finance", "days_present": 17, "daily_salary": 1100},
]

def calculate_salary(days_present,daily_salary):
    return days_present*daily_salary
def get_attendance_status(days_present):
    if days_present >= 22:
        return"Excellent"
    elif days_present >= 20:
        return"Good"
    elif days_present >= 18:
        return "Average"
    else:
        return"poor"
def calculate_bonus(basic_salary,attendance_status):
    if attendance_status == "Execellent":
        return basic_salary*0.05
    else:
        return 0
total_payroll = 0
highest_salary  = 0
highest_employee = ""
it_employee = 0
print("===========================================================================================")
print("                              EMPLOYEE PAYROLL REPORT                                      ")
print("===========================================================================================")
for employee in employees:
    basic_salary = calculate_salary(
        employee["day_present"],
        employee["daily_salary"]

    ) 
    attendance = get_attendance_status(
        employee["day_present"]
    )       
    bonus = calculate_bonus(
        basic_salary,
        attendance
    )
    final_salary  = basic_salary +bonus
    print(f"ID {employee} id")
    print(f"Name {employee} name")
    print(f"Department{employee} department")
    print(f"Attendance{attendance} ")
    print(f"Basic salary : Rs {basic_salary} ")
    print(f"Bonus : Rs {bonus} ")
    print(f"final salary : Rs{final_salary} ")
    total_payroll = final_salary
    if final_salary> highest_salary:
        highest_salary = final_salary
        highest_employee = employee["name"]
    if  employee["department"] == "IT":
     it_employee += 1  
average_salary = total_payroll/len(employees)
print("===============================================================")
print("                   COMPANY SUMMARY                             ")
print("===============================================================")
print(f"total employees ,len{employee}")  
print(f"total payroll   : {total_payroll}")
print(f"Average Salary : Rs {average_salary}")
print(f"Highest Paid Employees{highest_employee}")
print(f"IT Employees  {it_employee}")     