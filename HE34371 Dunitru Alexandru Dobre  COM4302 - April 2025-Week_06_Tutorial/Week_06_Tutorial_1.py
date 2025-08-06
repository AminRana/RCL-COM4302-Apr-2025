# a. Iterate characters and check vowels
word = input("Enter a word: ")
for char in word:
    if char.lower() in 'aeiou':
        print(f"{char} is a vowel")
    else:
        print(f"{char} is not a vowel")

# b. Add all even numbers up to 20
total = 0
for i in range(2, 21, 2):
    total += i
print("Total of even numbers up to 20:", total)

# c. Menu until Quit
while True:
    print("\n1. Add\n2. Search\n3. Update\n4. Delete\n5. Quit")
    choice = int(input("Choose: "))
    if choice == 5:
        print("Exiting...")
        break
    elif choice == 1:
        print("Added")
    elif choice == 2:
        print("Searched")
    elif choice == 3:
        print("Updated")
    elif choice == 4:
        print("Deleted")
    else:
        print("Invalid option")

# d. Prime check
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime")
            break
    else:
        print("Prime")
else:
    print("Not a prime")

# e. Series of prime numbers up to N
n = int(input("Enter upper limit: "))
for num in range(2, n + 1):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
print()

# f. Timetable for a number
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")