#Check Divisible by 3,5 and both
num=int(input('Enter Number :'))
if(num%3==0 and num%5==0):
    print('Divisible by both 3 and 5')
elif(num%3==0):
    print('Divisible by 3 only')
    
elif(num%5==0):
    print('Divisible by 5 only')

else:
    print('Divisible by none')