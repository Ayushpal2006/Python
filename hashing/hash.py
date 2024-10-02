##create an array
arr = [1,2,3,4,5,5,4,7,4]
l = len(arr)

hash  = [0]*13

for i in range(l):
    hash[arr[i]] = hash[arr[i]]+1

# for i in arr:
#     hash[i] = hash[i]+1
    
# a = int(input())
a = 5
while(a):
    value = int(input())
    print(hash[value])
    a=a-1
print(hash)
