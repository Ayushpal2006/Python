'''
1          1
12        21
12       321
1234    4321
12345  54321
123456654321

'''

n = int(input("Enter the Number : "))
 
for i in range(1,n+1):

    
        for j in range(1,i+1):  #star
            print(j, end="")
            
        for j in range(2*n-2*i):  #space
            print("",end=" ")
            
        for j in range(i,0,-1):  #star
            print(j, end="")
        
        
            
        print("")