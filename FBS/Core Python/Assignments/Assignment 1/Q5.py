principle=float(input('Enter Principle Amount :'))
time=float(input('Enter Time Period in months : '))
rate=float(input('Enter rate of Intrest :'))
FinalAmount=principle*(1+(rate/100))**time
CI=FinalAmount-principle
print(f'Compound Intrest={CI}')
