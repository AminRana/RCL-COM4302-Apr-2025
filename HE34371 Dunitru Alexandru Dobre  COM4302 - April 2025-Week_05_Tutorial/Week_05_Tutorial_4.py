# 4a) Grade with Validation
mark = int(input("Enter mark: "))
if 0 <= mark <= 100:
    if mark > 74:
        print("Distinction")
    elif mark >= 60:
        print("Merit")
    elif mark >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid mark")

# 4b) Check Character or Number
x = input("Enter first number: ")
y = input("Enter second number: ")
if x.isdigit() and y.isdigit():
    total = int(x) + int(y)
    print("Total:", total)
    if total > 100:
        print("Total is more than 100")
else:
    print("Inputs are not valid numbers")

# 4c) Menu with Validation
option = int(input("Choose (1–4): "))
if 1 <= option <= 4:
    if option == 1:
        print("Added")
    elif option == 2:
        print("Searched")
    elif option == 3:
        print("Updated")
    elif option == 4:
        print("Deleted")
else:
    print("Invalid input")

# 4d) Random Number Guess Loop
import random
while True:
    guess = int(input("Guess a number 1–5: "))
    rand = random.randint(1, 5)
    if guess != rand:
        print(f"Wrong! Random was {rand}. Ending.")
        break
    print("Correct! Try again.")

# 4e) Odd or Even Check with Range
num = int(input("Enter a number: "))
if 0 <= num <= 100:
    print("Even" if num % 2 == 0 else "Odd")
else:
    print("Out of range")