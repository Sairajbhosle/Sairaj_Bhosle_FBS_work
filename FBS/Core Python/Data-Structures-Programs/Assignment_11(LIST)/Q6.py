# Python Program to Find the Union of two Lists
li1=[1,2,3]
li2=[1,3,5]
for ele in li2[:]:
    if ele not in li1:
        li1.append(ele)


print(li1)


