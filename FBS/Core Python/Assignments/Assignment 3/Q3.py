#check leap year or not
year=int(input('Enter Year to Check :'))
if(year%4 or year%400 or year%100):
    print('Year is Leap Year')
else:
    print('Not a leap Year')
