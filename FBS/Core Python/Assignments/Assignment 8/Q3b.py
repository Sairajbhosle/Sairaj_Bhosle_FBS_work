def ser():
    n=int(input('Enter Range of Number :'))
    fact=1
    sum=0
    for i in range(1,n+1):
        fact=fact*i
        sum+=fact
    print(sum)
ser()
        