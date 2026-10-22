# Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

def evenodd(li):
    size=len(li)
    i=0
    even=[]
    odd=[]
    while(i<size):
        if(li[i]%2==0):
            even.append(li[i])
            i+=1
        else:
            odd.append(li[i])
            i+=1
    print(even)
    print(odd)


li=[2,3,9,5,4,98]

evenodd(li)