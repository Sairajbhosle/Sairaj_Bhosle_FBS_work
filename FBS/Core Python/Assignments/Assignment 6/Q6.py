
for i in range(1,7-1):
    count=0
    for j in range(1,7-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        count+=1
        print(count,end=' ')
    for j in range(1,i):
        count+=1
        print(count,end=' ')
    print()