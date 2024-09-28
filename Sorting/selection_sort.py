arr = [1,5,7,4,2,8]

for i in range(len(arr)):
    lastIndex = len(arr)-i-1
    maxi = max(arr[0:lastIndex+1])
    max_index = arr.index(maxi)
    
    arr[max_index],arr[lastIndex] = arr[lastIndex],arr[max_index]
    
print(arr)

