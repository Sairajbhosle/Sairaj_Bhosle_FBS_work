li=[10,20,2,45,34]
max=li[0]
min=li[0]
size=len(li)
for i in range(0,len(li)):
    if(li[i]>max):
        max=li[i]
print('Maximum :',max)

li=[10,20,2,45,34]
for i in range(0,len(li)):
    if(li[i]<min):
        min=li[i]

print('Minimum :',min)