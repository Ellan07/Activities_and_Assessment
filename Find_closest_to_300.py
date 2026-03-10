x = 300
def find_closest(a, b, c):
    diff_a = abs(a - x)
    diff_b = abs(b - x)
    diff_c = abs(c - x)

    smallest_diff = min(diff_a, diff_b, diff_c)

    if diff_a == diff_b == diff_c:
        return "All numbers are same equally closest to 300."

    elif smallest_diff == diff_a:
        return f"Letter A or {a} is the closest number to 300."
    elif smallest_diff == diff_b:
        return f"Letter B or {b} is the closest number to 300."
    else:
        return f"Letter C or {c} is the closest number to 300."


print("Find the closest number to 300")

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

result = find_closest(a, b, c)
print(result)