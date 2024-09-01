'''
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *

'''

n = int(input("Enter the Number: "))

# Print the upper part of the diamond
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print("")  # Move to the next line

# Print the lower part of the diamond
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")  # Move to the next line