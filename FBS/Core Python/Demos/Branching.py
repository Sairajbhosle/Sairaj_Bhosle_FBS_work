#if_else
num=int(input('Enter Number :'))
if(num%2==0):
   print('Even No')
else:
    print('Odd No')

#Nested_if_else
gender=(input('Enter Gender : (Male/Female)'))
age=int(input('Enter age :'))
if(gender=='Male'):
    if(age>=21):
        print('Eligible')
    else:
        print('Not Eligible')

else:
    
    if(age>=18):
        print('eligible')
    else:
        print('Not Eligible')
    