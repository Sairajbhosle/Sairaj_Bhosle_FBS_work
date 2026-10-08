n=int(input('Enter Number to Check:'))
r=0
c=0
temp=n
sum=0

def count():
    global n,c
  
    while(n>0):
        r=n%10
        c+=1
        n=n//10
def arm():  
    global n, c, sum
    n=temp
    while(n>0):
        d=n%10
        sum=sum+d**c
        n=n//10
    if(sum==temp):
        print('Armstrong')
    else:
        print('Not Armstrong')
count()
arm()
