def sum_digits(n):
    return sum(int(digit) for digit in str(n))

print("Sum of digits:", sum_digits(432))