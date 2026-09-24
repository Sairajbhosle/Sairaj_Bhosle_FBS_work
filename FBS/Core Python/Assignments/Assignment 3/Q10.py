gen=input('Enter Gender :')
age=int(input('Enter Age :'))
if(gen=='Male'):
    if(age>=21):
       print('Eligible for Marriage')
    else:
        print('Not Eligible')

else:
    if(age>=18):
        print('Female is Eligible')
    else:
        print('Not Eligible')

