#check Grade
mark1=int(input('enter marks of Subject 1 out of 100 :'))
mark2=int(input('enter marks of Subject 2 out of 100 :'))
mark3=int(input('enter marks of Subject 3 out of 100 :'))
mark4=int(input('enter marks of Subject 4 out of 100 :'))
mark5=int(input('enter marks of Subject 5 out of 100 :'))
Total=mark1+mark2+mark3+mark4+mark5
if(Total>450):
    print('Grade A')
elif(Total>400):
    print('Grade B')
elif(Total>350):
    print('Grade C')
else:
    print('Grade D')
