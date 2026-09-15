days=int(input('Enter Number Of Days ='))
year=days//365
ndy=days%365
week=ndy//7
nndy=week%7
#remaindays=days%7
print(f'Number of Years={year}')
print(f'Number of week={week}')

#print(f'Number of Remaining days in week={remaindays}')
print(f'Number of Remaining days={nndy}')




