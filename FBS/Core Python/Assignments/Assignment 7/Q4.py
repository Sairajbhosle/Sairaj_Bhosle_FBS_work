count=0
flag=1
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(i):
        print(i+j,end=' ')
    for j in range(i-2,-1,-1):
        print(i+j,end=' ')
        

    print()
        