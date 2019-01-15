# Cube Comprehension
numbers = [number ** 3 for number in (range(1, 11, 1))]
print(numbers)
print("The first three items in the list are:")
for number in numbers[:3]:
    print(number)
print("The three middle items in the list are:")
for number in numbers[5:8]:
    print(number)
print("The last three items in the list are:")
for number in numbers[-3:]:
    print(number)
