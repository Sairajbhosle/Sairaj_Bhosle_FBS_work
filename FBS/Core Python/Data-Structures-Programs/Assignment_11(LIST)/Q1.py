# Python Program to Put Even and Odd elements of a List into two Different
# # Lists
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