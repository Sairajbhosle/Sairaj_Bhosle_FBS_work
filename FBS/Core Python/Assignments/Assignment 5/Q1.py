# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.
count=3
for i in range(1,count+1):
    id=(input('Enter User Id :'))
    pas=int(input('Enter User Pass :'))
    pas1=123

    id1='Sai'
    if(id==id1 and pas==pas1):
        print('Valid Id and Password')
        print('Access Granted')
        break
    else:
        print('Invalid Credentials Re-Enter')
        continue

    

            

    
    
        
