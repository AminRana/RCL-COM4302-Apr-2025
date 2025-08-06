def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "Cannot divide by zero"

def menu_calc():
    while True:
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit")
        choice = input("Choose option: ")
        if choice == "5":
            break
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", sub(a, b))
        elif choice == "3":
            print("Result:", mul(a, b))
        elif choice == "4":
            print("Result:", div(a, b))
        else:
            print("Invalid option")

menu_calc()