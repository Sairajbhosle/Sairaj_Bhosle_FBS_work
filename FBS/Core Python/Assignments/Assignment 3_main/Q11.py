age=int(input('Enter Age :'))
amount=2000
if(age>59):
    print('Senior citizen Discount=50%')
    Dis=amount*50/100
    ta=amount-Dis
    print(f'Total amount to pay={amount-Dis}')
elif(age<12):
    print('Children Discount=30%')
    Dis=amount*30/100
    ta=amount-Dis
    print(f'Total amount to pay={amount-Dis}')
else:
    print(f'No Discount-Total amount to pay :{amount}')
    ta=amount
age=int(input('Enter Age :'))
amount=2000
if(age>59):
    print('Senior citizen Discount=50%')
    Dis1=amount*50/100
    ta1=amount-Dis1
    print(f'Total amount to pay={amount-Dis1}')
elif(age<12):
    print('Children Discount=30%')
    Dis1=amount*30/100
    ta1=amount-Dis1
    print(f'Total amount to pay={amount-Dis1}')
else:
    print(f'No Discount-Total amount to pay :{amount}')
    ta1=amount


totalpay=ta+ta1
print(f'Total Amount to Pay={totalpay}')












