#Python Program to Sort the List According to the Second Element in Sublist
def secondSort(li):
    size=len(li)
    for i in range(size):
        for j in range(i+1,size):
            if li[i][1]>li[j][1]:
                li[i],li[j]=li[j],li[i]
    print(li)

        

li=[[10,2],[1,13],[22,12]]
secondSort(li)