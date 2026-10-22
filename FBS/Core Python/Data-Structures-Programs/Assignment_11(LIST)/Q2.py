# Python Program to Merge Two Lists and Sort it
def merge(li1,li2):
    size=len(li2)
    for ele in li2 [:]:
        li1.append(ele)
    li1.sort()
    print(li1)

li1=[10,20,11]
li2=[22,33,1,2]
merge(li1,li2)