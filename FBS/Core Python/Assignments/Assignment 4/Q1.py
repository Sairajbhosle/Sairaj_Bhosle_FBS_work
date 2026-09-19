#calculator
num1=int(input('Enter Number 1 :'))
num2=int(input('Enter Number 2 :'))
operator=input('Enter Operator :')
if(operator== '+'):
    print(num1+num2)
elif(operator == '-'):
    print(num1-num2)
elif(operator == '*'):
    print(num1*num2)
elif(operator == '/'):
    print(num1/num2)
else:
    print(num1%num2)
