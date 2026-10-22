# Python Program to Find the Second Largest Number in a List Using Bubble
# Sort
def bubble(li):
    size=len(li)
    for i in range(1,size):
        for j in range(0,size-i):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    print('Second Largest=',li[size-2])





li=[10,1,33,22,21]
bubble(li)