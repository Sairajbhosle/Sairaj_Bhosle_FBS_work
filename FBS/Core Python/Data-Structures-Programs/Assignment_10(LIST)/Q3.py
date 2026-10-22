li=[10,30,20,40]
size=len(li)
max=li[0]
sec_large=0
for i in range(0,size):
    if(max<li[i]):
        sec_large=max
        max=li[i]
    elif(li[i]>sec_large):
        sec_large=li[i]
print('MAX=',max)
print('SECOND LARGE=',sec_large)

