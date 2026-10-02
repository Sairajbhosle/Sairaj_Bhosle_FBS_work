 #geometric series 
#a + ar + ar^2 + ar^3 
a=int(input('Enter Series no :'))
r=2
n=int(input('enter range of n :'))
sum1=0
for i in range(0,n):
    sum1=sum1+(a*(r**i))
print(sum1)




