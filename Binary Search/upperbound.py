import bisect
lst = [1, 3, 4, 4, 5]
index = bisect.bisect_left(lst, 4)
print(index)  # Output: 2

indexx = bisect.bisect_right(lst, 4)
print(indexx)  # Output: 4