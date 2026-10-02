# WAP to print Armstrong number within a given range
start=int(input('Enter range From where to start :'))
end=int(input('Enter where to end :'))
for i in range(start,end+1):
    count=0
    temp=i
    temp1=temp
    temp2=i
    sum=0
    while(temp2>0):
        d=temp2%10
        count+=1
        temp2=temp2//10
    while(temp>0):
        r=temp%10
        sum=sum+(r**count)
        temp=temp//10
    if(temp1==sum):
        print(temp1)
    