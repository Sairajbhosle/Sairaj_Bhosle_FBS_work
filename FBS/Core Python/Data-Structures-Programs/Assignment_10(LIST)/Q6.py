# Write a program to remove duplicates from the list.
def duplicate(li):
    new=[]
    for i in li:
        if i not in new:
            new.append(i)
    print(new)
li=[10,20,10,30,21,11,20,11]
duplicate(li)

# same list
def duplicate(li):
    i = 0
    while i < len(li):
        j = i + 1
        while j < len(li):
            if li[i] == li[j]:
                li.pop(j)
            else:
                j += 1
        i += 1
    print(li)

li = [10,20,30,10,20,40,55]
duplicate(li)