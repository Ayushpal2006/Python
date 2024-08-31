name = input("Enter the Name : ")

str_1 = name
str_2 = name[::-1]

if(str_1 == str_2 ):
    print("this is Palindrome")

else:
    print("This is not Palindrome")