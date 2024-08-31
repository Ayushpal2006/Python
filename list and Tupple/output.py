A = []

for i in range(0,5):
    A.append(i)
print(A)

## question 2

b = [1,2,3,4,5]
print(b[3:0:-1])

## question 3
t = tuple(b)
print(t)

## question 4
t1 = 'a','b'
t2 = ('a','b')
print(t1 == t2)

## question 5
t3 = (((('a',1),'b','c'),'d',2),'e',3)
print(len(t3))

## question 6
A = ('Hello','Harsh','How\'re','you?')
(a,b,c,d) = A
print(a,b,c,d)
A =(a,b,c,d)
print(A[0][0]+A[1][1],A[1])