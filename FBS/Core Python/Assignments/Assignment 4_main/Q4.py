#Factorial
n=int(input('Enter no :'))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f'Factorial={fact}')