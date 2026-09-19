#check discounted amount for students
stud=input('Enter You are student or not :')
if(stud=='yes'):
    amount = int(input('Enter Amount of items Purchased :'))
    if(amount>500):
        Dis=amount*20/100
        Dis_amount=amount-Dis
        print(f'20 percent Discount : Discounted Amount : Total to Pay :{Dis_amount}')
    else:
        Dis=amount*10/100
        Dis_amount=amount-Dis
        print(f'10 percent Discount : Discounted Amount : Total to Pay :{Dis_amount}')
else:
    amount = int(input('Enter Amount of items Purchased :'))
    if(amount>600):
        Dis=amount*15/100
        Dis_amount=amount-Dis
        print(f'15 percent Discount : Discounted Amount : Total to Pay :{Dis_amount}')
    else:
        print('No Discount')