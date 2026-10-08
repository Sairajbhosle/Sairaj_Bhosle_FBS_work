def prime():
    ran=int(input('Enter No :'))
    n=0
    num=2
    sum=0
    while(n<ran):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            sum+=num
            n+=1
        num+=1
    print(sum)
prime()
        
