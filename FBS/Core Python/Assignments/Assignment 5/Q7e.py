# x - x2/3 + x3/5 - x4/7 + .... to n terms
a=int(input('Enter no :'))
sum1=0
for i in range(1,a+1):
    if(i%2==0):
        sum1=sum1-(a**i)/(2*i-1)
    else:
        sum1=sum1+(a**i)/(2*i-1)


print(sum1)