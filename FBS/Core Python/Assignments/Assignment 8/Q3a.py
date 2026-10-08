def ser():
    n=int(input('Enter Range Number :'))
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(f'Sum of Series :{sum}')
ser()