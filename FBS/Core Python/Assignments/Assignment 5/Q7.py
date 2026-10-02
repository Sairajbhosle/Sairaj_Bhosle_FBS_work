n=int(input('Enter Range :'))
num=1
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    #print(fact)
    sum+=fact
print(sum)
        
