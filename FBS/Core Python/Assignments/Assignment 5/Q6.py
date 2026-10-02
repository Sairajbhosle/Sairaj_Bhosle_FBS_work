#Write a program to print first n prime numbers.
n=0
num=2
ran=int(input('Enter Range : '))
while(n<ran):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num)
        n+=1
    num+=1

        


    