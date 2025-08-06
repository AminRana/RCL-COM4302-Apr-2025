def run_cumulative():
    total = 0
    while True:
        n = int(input("Type your number: "))
        total += n
        print("Your total:", total)
        again = input("Will you run the program again (yes/no)? ")
        if again.lower() != "yes":
            break

run_cumulative()