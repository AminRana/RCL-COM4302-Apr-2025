col = "   regent college London   "

# a)
col2 = col.strip()
print("col2:", col2)

# b)
print(col2.lower())

# c)
print(col2.title())

# d)
print(col2.upper())

# e)
print("college" in col2)

# f)
print(col2.replace("college", "university"))

# g)
print(col2.isalpha())  # False because of spaces