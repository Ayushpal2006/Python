arr = [1,5,7,4,2,8]
l = len(arr)

for i in range(0,l-1):
    for j in range(i+1,0,-1):
        if(arr[j]<arr[j-1]):
            #swap:
            arr[j-1],arr[j] = arr[j],arr[j-1]

print(arr)