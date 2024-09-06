# inserting 
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr, "before")

arr[0][0] = 1 # update only one element
print(arr, "after")
# accesing
arr=[[1,2,3],[4,5,6],[7,8,9]]

print("Element at [1][0]=",arr[0])

# traverse

arr=[[1,2,3],[4,5,6],[7,8,9]]

for i in arr:
    for j in i:
        print(j,end=" ")
    print()
    

