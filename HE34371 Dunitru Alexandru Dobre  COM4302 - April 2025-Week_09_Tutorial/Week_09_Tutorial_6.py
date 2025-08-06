fruits = ["apple", "banana", "mango", "grape", "kiwi", "lemon", "peach", "plum", "berry", "melon"]

def print_fruits():
    print(fruits)

def count_chars():
    for fruit in fruits:
        print(f"{fruit}: {len(fruit)} characters")

def add_fruit(fruit):
    fruits.append(fruit)

print_fruits()
count_chars()
add_fruit("orange")
print_fruits()