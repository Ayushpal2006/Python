from collections import deque

d = deque([1, 2, 3])
d.append(4)       # Add to the right end
d.appendleft(0)   # Add to the left end
print(d)          # Output: deque([0, 1, 2, 3, 4])
d.pop()           # Remove from the right end
d.popleft()       # Remove from the left end
