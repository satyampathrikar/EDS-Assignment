from datetime import datetime

birth_year = int(input("Enter birth year: "))
salary_rupees = float(input("Enter salary in INR: "))

current_year = datetime.now().year
age = current_year - birth_year

salary_dollars = salary_rupees / 83  # approx conversion

print("Age:", age)
print("Salary in USD:", salary_dollars)