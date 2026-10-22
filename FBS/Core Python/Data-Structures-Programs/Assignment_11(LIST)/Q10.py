# 10. Write a program to print list after removing even numbers.
def odd(li):
    size=len(li)
    i=0
    oddd=[]
    while(i<size) :
        if(li[i]%2!=0):
            oddd.append(li[i])
        i+=1
    print(oddd)
li=[10,20,30,11,23,45]
odd(li)