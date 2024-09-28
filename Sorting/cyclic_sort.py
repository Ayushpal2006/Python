# arr = [1,2,3,4,5,6,7]
arr = [1,5,2,4,3,7,6]
l= len(arr)
i = 0

while(i<l):
    index = arr[i]-1
    if(arr[i]!=arr[index]):
        #swap
        arr[i],arr[index] = arr[index],arr[i]
    else:
        i = i+1
        
print(arr)