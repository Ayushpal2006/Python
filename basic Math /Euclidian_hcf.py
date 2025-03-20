
def hcf(a, b):
    while(a>0 and b>0):
        if(a>b):
            a=a%b
        else:
            b= b%a
            
    if(a==0):
        print(b)
    
    print(a)
hcf(20, 40)