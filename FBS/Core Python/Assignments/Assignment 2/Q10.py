num=int(input('Enter Your Number to be Reversed :'))
rev=0
d1 = num%10
rev=rev*10+d1
num=num//10

d2= num%10
rev=rev*10+d2
num=num//10

d3=num%10
rev=rev*10+d3

print(rev)