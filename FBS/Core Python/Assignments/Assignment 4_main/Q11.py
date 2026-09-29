#WAP to check if given number Strong Number.
n=int(input('Enter No='))
temp=0
temp=n
sum=0
while(n!=0):
    d=n%10
    n=n//10
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    sum+=fact

if(sum==temp):
    print('Strong no')
else:
    print('Not Strong')
    


