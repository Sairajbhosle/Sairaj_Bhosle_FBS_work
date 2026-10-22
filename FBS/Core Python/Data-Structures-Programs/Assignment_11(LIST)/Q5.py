#Python Program to Sort a List According to the Length of the Elements
# within the list.
def bubble(li):
    size=len(li)
    for i in range(1,size):
        for j in range(0,size-i):
            if len(li[j])>len(li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
    print('Sorted=',li)

li=[[12,23,1],[33,22],[21,1,23,2]]
bubble(li)