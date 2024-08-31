# 0,1,1,2,3,5,8,13

def fabo(n):
    count = 0     
    a= 0
    b=1
    while(count<n):
        print(a)
        temp = a+b
        a = b
        b = temp
        count = count + 1
        
    
    
    print(a)

    
n = int(input("Enter the term : "))
fabo(n)