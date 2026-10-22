#Write a program to create a new list from existing list which contains cube of
#each number of list.
def cube(li):
    new=[]
    size=len(li)
    i=0
    while i<size:
        new.append(li[i]**3)
        i+=1
    print(new)

li=[1,3,5,7]
cube(li)
