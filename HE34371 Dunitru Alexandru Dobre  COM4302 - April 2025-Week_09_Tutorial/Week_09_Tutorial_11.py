import random

def pick_random(fruits_list):
    index = random.randint(0, len(fruits_list) - 1)
    return fruits_list[index]

fruits = ["apple", "banana", "mango", "orange", "kiwi"]
print("Random fruit:", pick_random(fruits))