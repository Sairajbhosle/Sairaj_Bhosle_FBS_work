#Check child,teen,adult,senior
age=int(input('Enter Age :'))
if(age>60):
    print('Senior')
elif(age>20 and age<59):
    print('Adult')
elif(age>12 and age<19):
    print('Teenager')
else:
    print('Child')