'''
Input Format: N = 3
Result: 
1
1 2 
1 2 3

'''

n = int(input("Enter the Number : "))
 
for i in range(1,n+1):
        for j in range(1,i+1):
            print(j , end="")
        
        print("")