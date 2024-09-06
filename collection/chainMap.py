from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)
print(chain['b'])  # Output: 2 (from the first dictionary)
print(chain['c'])  # Output: 4 (from the second dictionary)
