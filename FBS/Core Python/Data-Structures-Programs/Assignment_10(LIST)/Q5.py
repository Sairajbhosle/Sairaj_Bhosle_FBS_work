#Accept a number from user and check if this element is present in the list or
#not. Also tell how many times it is present in the list.

li=[10,20,10,30,22,45,20]
size=len(li)
count=0
ele=int(input('Enter element to check :'))
for i in range(0,size):
    if li[i]==ele:
        count+=1
if count>0:
    print('Element present')
else:
    print('element not present')
print('Element count=',count)