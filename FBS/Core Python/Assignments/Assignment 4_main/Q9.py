#WAP to print all numbers in a range divisible by a given number.
stn=int(input('Enter No to start :'))
eno=int(input('Enter num to end :'))
div=int(input('Enter no to divide :'))
for i in range(stn,eno+1):
    if(i%div==0):
        print('Numbers is divisible ',i)