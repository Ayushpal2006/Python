dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Unpacking dict1 into dict2
combined_dict = {**dict1, **dict2}
merged_dict = dict1 | dict2


print(combined_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}]
print(merged_dict)


