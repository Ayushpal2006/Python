arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(arr)

# Step 1: Create a temporary array to store the rotated values
temp = [0] * n

# Step 2: Place each element in the rotated position
for i in range(n):
    temp[(i + k) % n] = arr[i]

for i in range(n):
    arr[i] = temp[i]


print(arr)
