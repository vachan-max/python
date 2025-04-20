numbers = [1, 2, 31, 2, 3, 4, 6, 5, 44, 2, 3, 4, 5, 6, 7, 8, 9, 0]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(numbers[5])  # Prints the element at index 4
print(frequency) 