'''
Input Format: N = 3
Result: 
A
A B
A B C
A B C D
A B C D E
A B C D E F

'''

n = int(input("Enter the Number : "))
 
for i in range(1,n+1):
        for j in range(0,i):
            print(chr(65+j) , end="")
        
        print("")

