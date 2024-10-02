def kadane(arr):
    n = len(arr)
    maxi = 0
    curr_sum = 0
    
    for i in range(n):
        curr_sum += arr[i]
        maxi = max(maxi,curr_sum)

        if curr_sum < 0:
            curr_sum = 0
        
    return maxi
    
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane(arr))

