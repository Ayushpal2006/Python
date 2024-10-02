def prefix(arr):
    n = len(arr)
    pre_arr = [0]*n
    pre_arr[0] = arr[0]
    
    for i in range(1,n):
        pre_arr[i] = pre_arr[i-1] + arr[i]
    
    return pre_arr

arr = [1,2,3,4,5]
print(prefix(arr))

