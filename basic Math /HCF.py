
def hcf(a, b):
    hcf = 1
    for i in range( min(a, b) + 1,0,-1):
        
        if (a % i == 0) and (b % i == 0):
            hcf = i
            break
        
    print(hcf)

hcf(20, 40)

