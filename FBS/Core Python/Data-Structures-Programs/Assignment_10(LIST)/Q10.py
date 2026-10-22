# Write a program to remove all occurrences of a given element in the list.
def rem(li):
    ele=int(input('Enter element to remove its occurrences'))
    i=0
    size=len(li)
    while i<len(li):
        if li[i]==ele:
            li.remove(li[i])
        else:
            i+=1
    print(li)
li=[10,20,30,10,40]
rem(li)



