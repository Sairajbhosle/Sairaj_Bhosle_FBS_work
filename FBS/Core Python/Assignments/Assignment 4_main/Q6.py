#Prime No
n=int(input('Enter No :'))
for i in range(2,int(n/2)):
    if(n%i==0):
        print(f'Not Prime={n}')
        break
else:
    print(f'Prime no={n}')
        

