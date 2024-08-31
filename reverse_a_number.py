
def reverse(num):
    digit = 0
    while(num>0):
        rem = (num % 10)
        digit = digit*10 + rem
        # num = int(num/10)
        num = num //10
        
    return digit
         

x = int(input("Enter the number : "))
y = reverse(x)
print(y)

def reverse_using_string(num):
    sting_num = str(num)
    
    return int(sting_num[::-1])

a = 123456
b = reverse_using_string(a)
# print(f"This is reversed number : {b}",)