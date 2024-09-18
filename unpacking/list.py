my_list = [1, 2, 3]
a, b, c = my_list

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

##second form

my_list = [1, 2, 3, 4, 5]
a, b, *rest = my_list

print(a)    # Output: 1
print(b)    # Output: 2
print(rest) # Output: [3, 4, 5]