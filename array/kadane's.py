def euqal_sum(arr):
    n = len(arr)
    total_sum = 0,
    prefix_sum = 0
    
    #total sum
    total_sum = sum(arr)
    
    for i in range(n):
        prefix_sum += arr[i]
    
        ans = total_sum - prefix_sum
        if (ans == prefix_sum):
            return 1
    return 0

arr = [2,4,6,2,1,5,8,2]
print(euqal_sum(arr))

