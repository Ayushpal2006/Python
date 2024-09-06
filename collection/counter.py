from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
count = Counter(words)
print(count)  # Output: Counter({'banana': 3, 'apple': 2, 'orange': 1})
