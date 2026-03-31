def closest_to_300(numbers):
    closest = numbers[0]

    for num in numbers:
        if abs(num - 300) < abs(closest - 300):
            closest = num

    return closest

user_input = input("Enter a number: ")

nums = []
for x in user_input.split():
    nums.append(int(x))

result = closest_to_300(nums)

print("Closest to 300:", result)
