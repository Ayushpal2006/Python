'''
***********
 *********
  *******
   ***** 
    ***    
     *

'''

n = int(input("Enter the Number : "))
 
for i in range(n):

        for j in range(i):  #space
            print("",end=" ")

        for j in range((2*(n-i))-1):  #star
            print("*", end="")
        
        
        for j in range(i):  #space
            print("",end=" ")
            
        print("")