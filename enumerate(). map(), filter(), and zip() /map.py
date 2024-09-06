numbers = [1, 2, 3, 4, 5]
def square(num):
    return num ** 2

squared_numbers = list(map(square, numbers))
print(squared_numbers)

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

