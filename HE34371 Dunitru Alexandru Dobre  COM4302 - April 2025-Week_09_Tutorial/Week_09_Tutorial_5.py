def total(numbers):
    return sum(numbers)

def average(numbers):
    return sum(numbers) / len(numbers)

def maximum(numbers):
    return max(numbers)

nums = [12, 34, 23, 45, 56]
print("Total:", total(nums))
print("Average:", average(nums))
print("Max:", maximum(nums))