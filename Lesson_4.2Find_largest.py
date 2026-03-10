def find_largest(a, b, c):
    largest = max(a, b, c)

    if largest == a:
        letter = 'a'
    elif largest == b:
        letter = 'b'
    else:
        letter = 'c'

    return letter, largest


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

letter, value = find_largest(a, b, c)

print(f"Letter '{letter}' has the largest number with a value of {value}.")
