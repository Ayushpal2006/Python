def suffix(arr):
    n = len(arr)
    suf_arr = [0]*n
    suf_arr[n-1] = arr[n-1]
    
    for i in range(n-2,-1,-1):
        suf_arr[i] = suf_arr[i+1] + arr[i]
    
    return suf_arr

arr = [1,2,3,4,5]
print(suffix(arr))