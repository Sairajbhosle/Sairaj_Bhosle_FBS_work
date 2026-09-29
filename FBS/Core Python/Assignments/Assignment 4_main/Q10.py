#WAP to check if given number is Perfect Number.
n=int(input('Enter No :'))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum==n):
    print('prefect no')
else:
    print('Not Prefect')
    