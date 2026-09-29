#Write a program to check if given number is Armstrong number or not.
n=int(input('Enter No='))
temp1=n
temp=n
sum1=0
count=0
while(n>0):
    d=n%10
    count+=1
    n=n//10
while(temp>0):
    r=temp%10
    sum1=sum1+(r**count)
    temp=temp//10

if(sum1==temp1):
    print('Armstrong')
else:
    print('Not Armstrong')


    