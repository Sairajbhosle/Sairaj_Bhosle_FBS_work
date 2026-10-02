# Write a program to print prime numbers between 1 to 100.
for i in range(2,100+1):
    num=i
    for j in range(2,num):
        if(num%j==0):
            break            
    else:
        print(num)    
