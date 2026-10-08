def ser():
    sum=0
    a=0
    count=1
    n=int(input('Enter Range of Number :'))
    for i in range(1,n+1):
        a=i*count
        count+=1
        sum+=a
    print(sum)
ser()