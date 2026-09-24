#Check no is Palindrome or Not
num=int(input('Enter 3 digit number :'))
temp=num
rev_num=0
d1=num%10
rev_num=rev_num*10+d1
num=num//10
d2=num%10
rev_num=rev_num*10+d2
num=num//10
d3=num%10
rev_num=rev_num*10+d3
num=num//10

if(temp==rev_num):
    print('Palindrome Number')
else:
    print('Not Palindrome')




