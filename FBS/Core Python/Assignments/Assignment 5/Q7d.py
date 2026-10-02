# S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a=int(input('Enter no :'))
sum1=0
for i in range(0,a):
    sum1=sum1+(a**i)/i
print(sum1)
