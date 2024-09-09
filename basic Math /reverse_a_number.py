
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
    string_num = str(num)
    res = 0
    
    if string_num[0] == '-':
        res =  int('-' + string_num[:0:-1])
    else:
        res = int(string_num[::-1])

    if res > 2 ** 31 - 1 or res < -2 ** 31:
        return 0
        
    return res

a = -123
b = reverse_using_string(a)
print(f"This is reversed number : {b}",)