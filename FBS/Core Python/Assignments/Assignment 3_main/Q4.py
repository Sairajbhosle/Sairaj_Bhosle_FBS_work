# Check Wheather it is Triangle or not on sides
#Triangle Comparision can be done using and also
side1=int(input('Enter Side 1 :'))
side2=int(input('Enter Side 2 :'))
side3=int(input('Enter Side 3 :'))
if(side1+side2>side3):
    print('It is a Triangle')
elif(side2+side3>side1):
    print('It is a triangle')
elif(side3+side1>side1):
    print('It is triangle')
else:
    print('Not a triangle')
  