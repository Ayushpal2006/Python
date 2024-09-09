def arms(n):
    ans = 0
    m = n
    while(n>0):
        digit = n%10
        n = n//10
        ans= ans + digit*digit*digit
        
        if(n==0):
            break
        
    if(ans == m):
        print("this is amstrong Number")

    else:
        print("Not a amstrong NUmber")
        
N = int(input("Enter the Number  :"))
arms(N)