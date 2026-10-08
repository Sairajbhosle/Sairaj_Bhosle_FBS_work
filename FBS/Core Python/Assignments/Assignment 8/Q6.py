def fab():

    a=-1
    b=1
    n=int(input('Enter No of range :'))
    for i in range(1,n):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
fab()
