def divisor(n):
    
    
    
    for i in range(1,n):
        if n%i==0:
            print(f"Is the divisor of {n}-->{i}, ")
                


n = int(input("Enter the number : "))
divisor(n)