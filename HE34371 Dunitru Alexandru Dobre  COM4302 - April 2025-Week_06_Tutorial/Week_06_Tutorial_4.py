nums = [3, 7, 19, 2, 8, 3, 9, 1, 6]

# a. Append 4
nums.append(4)

# b. Insert 23 between 2 and 8
index = nums.index(2) + 1
nums.insert(index, 23)

# c. Print 5th to 7th
print(nums[4:7])

# d. Add [3,6,9,12]
nums += [3, 6, 9, 12]

# e. Reverse
nums.reverse()

# f. Delete 4th
if len(nums) >= 4:
    del nums[3]

# g. Sort descending
nums.sort(reverse=True)

# h. Print all odd numbers
print([n for n in nums if n % 2 == 1])

# i. Add all numbers
print("Sum:", sum(nums))