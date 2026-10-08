def add():
    sum=0
    n=int(input('Enter No :'))
    for i in range(1,n+1):
        d=n%10
        sum+=d
        n=n//10
    print(sum)
add()
