words = ['jam', 'argue', 'elf', 'brown', 'dice', 'dingo']

# a. Add 'poster'
words.append('poster')

# b. Add 'bin' between elf and brown
words.insert(3, 'bin')

# c. Reverse the list
words.reverse()

# d. Remove 'dice'
if 'dice' in words:
    words.remove('dice')

# e. Add new list
words += ['table', 'brave', 'cat']

# f. Create newWords
newWords = words[1:4]

# g. UPPER CASE
print([w.upper() for w in words])

# h. Title CASE
print([w.title() for w in words])

# i. Last three items
print(words[-3:])