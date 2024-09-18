D = {}
D[(1,2,4)]=8
D[(4,2,1)]=10
D[(1,2)]=12

sum = 0
for i in D:
    print(i)
    sum = sum+D[i]


print(sum)    
print(D)


