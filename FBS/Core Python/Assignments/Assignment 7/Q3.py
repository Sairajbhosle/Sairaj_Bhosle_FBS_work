count=0
flag=1
for i in range(1,6):
    for j in range(1,i+1):
        
        if(i==j):
            count+=1
            print(count,end=' ')
        elif(j==1):
            print('1',end=' ')
        elif(i==5):
            flag+=1
            print(flag,end=' ')
        else:
            print(' ',end=" ")
        
    print()