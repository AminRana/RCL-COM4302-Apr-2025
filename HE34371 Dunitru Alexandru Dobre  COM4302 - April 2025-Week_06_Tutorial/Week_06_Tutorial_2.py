# a. Numbers with power values
for i in range(1, 7):
    print(f"{i} = {i}, {i**2}, {i**3}, {i**4}")

# b. 1 to 50 in 5 lines
for i in range(1, 51, 10):
    print(list(range(i, i + 10)))

# c. Patterned rows: 0–3, 10–13, ..., 100–103
for row in range(0, 101, 10):
    print([row + i for i in range(4)])

# d. Timetable up to 10
for i in range(1, 11):
    print(f"{i} =", end=' ')
    for j in range(1, 11):
        print(f"{i}x{j}={i*j}", end=' ')
    print()