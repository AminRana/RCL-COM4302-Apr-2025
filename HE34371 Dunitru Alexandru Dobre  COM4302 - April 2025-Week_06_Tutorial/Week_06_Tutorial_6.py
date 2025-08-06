items = ['apple', 'banana', 'cherry']
while True:
    print("\n1. Display\n2. Add\n3. Delete\n4. Quit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print(items)
    elif choice == 2:
        new_item = input("Enter item to add: ")
        items.append(new_item)
    elif choice == 3:
        del_item = input("Enter item to delete: ")
        if del_item in items:
            items.remove(del_item)
    elif choice == 4:
        break
    else:
        print("Invalid")