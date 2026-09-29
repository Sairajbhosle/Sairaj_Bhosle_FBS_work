# fabonacci series
a=-1
b=1
c=0
n=int(input('Enter no='))
for i in range(0,n+1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
