principle=float(input('Enter Principle Amount :'))
time=float(input('Enter Time Period in months : '))
rate=float(input('Enter rate of Intrest :'))
SI=(principle*time*rate)/100
print(f'Simple Intrest={SI}')
Compound=SI+((SI*rate)/100)
print(Compound)