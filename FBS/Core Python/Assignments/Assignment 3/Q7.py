#check total salary
salary=int(input('Enter Basic Salary :'))
if(salary<=5000):
    da=salary*10/100
    ta=salary*20/100
    hra=salary*25/100
    print(f'Total Salary ={salary+da+ta+hra}')
else:
    da=salary*15/100
    ta=salary*25/100
    hra=salary*30/100
    print(f'Total Salary ={salary+da+ta+hra}')