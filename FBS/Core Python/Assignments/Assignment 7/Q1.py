for i in range(1,6):
    for j in range(6,0,-1):
        if(i==j):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(2,6):
        if(i==j):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

for i in range(2,7):
    for j in range(1,6):
        if(i==j):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(6,0,-1):
        if(i==j):
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()


    
    