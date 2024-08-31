f = open("poem.txt",'r')
p = f.read()
s= p.split()
word ="twinkle"

for i in s:
    if word in s:
        print("Find word twinkel")
        break
    else:
        print("not find")
        