def leap():
    y=int(input('Enter Year To Check :'))
    if(y%4==0):
        print('Leap Year')
    elif(y%100):
        print('Not a Leap Year')
    elif(y%400):
        print('Leap Year')
leap()
