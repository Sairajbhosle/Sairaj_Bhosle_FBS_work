# Program to Find the Intersection of Two Lists
li1=[1,2,3]
li2=[1,3,5]
li3=[]
for ele in li2[:]:
    if ele in li1:
        li3.append(ele)


print(li3)


