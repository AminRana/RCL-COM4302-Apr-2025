# 3a) Grade Calculator
mark = int(input("Enter mark: "))
if mark > 74:
    print("Distinction")
elif mark >= 60:
    print("Merit")
elif mark >= 40:
    print("Pass")
elif mark >= 0:
    print("Fail")
else:
    print("Invalid mark")

# 3b) Word Length Evaluation
word = input("Enter a word: ")
length = len(word)
if 1 <= length <= 3:
    print("too short word")
elif 4 <= length <= 8:
    print("small word")
elif 9 <= length <= 12:
    print("big word")
else:
    print("too big word")

# 3c) Menu Option
print("1. Add\n2. Search\n3. Update\n4. Delete")
option = int(input("Choose (1–4): "))
if option == 1:
    print("Added")
elif option == 2:
    print("Searched")
elif option == 3:
    print("Updated")
elif option == 4:
    print("Deleted")

# 3d) Profession Hourly Rate
profession = input("Enter profession: ").lower()
rates = {"teacher": 25, "doctor": 60, "lawyer": 200, "driver": 15}
print(f"Hourly rate: £{rates.get(profession, 'Unknown profession')}")

# 3e) Tax and Net Salary
salary = float(input("Enter gross salary: "))
if salary <= 12570:
    tax = 0
elif salary <= 50270:
    tax = (salary - 12570) * 0.2
elif salary <= 125140:
    tax = (50270 - 12570) * 0.2 + (salary - 50270) * 0.4
else:
    tax = (50270 - 12570) * 0.2 + (125140 - 50270) * 0.4 + (salary - 125140) * 0.45
print(f"Tax: £{tax}, Net Salary: £{salary - tax}")