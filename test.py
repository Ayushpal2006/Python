numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
sorted_numbers = numbers.sort()

print(numbers)  # [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

for i, num in enumerate(numbers):
    print(f'i = {i}, num == {num}')
    

