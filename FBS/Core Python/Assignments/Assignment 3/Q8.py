#Check 
id=input('Enter Userid :')
pass1=int(input('Enter Pass :'))
Userid='Sai'
password=123
if(id==Userid and password==pass1):
    print('Login Done')
    Captcha=987
    print(f'Captcha={Captcha}')
    c=int(input('Enter the Captcha given:'))
    if(c==Captcha):
        print('Success')
    else:
        print('Enter Valid Captcha')
else:
    print('invalid credentials')