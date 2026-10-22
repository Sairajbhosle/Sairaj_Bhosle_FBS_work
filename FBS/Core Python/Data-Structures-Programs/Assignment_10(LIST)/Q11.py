# Write a program to print all numbers which are divisible by m and n in the
# list.
def divisible(li):
    m=2
    n=3
    for ele in li [:]:
        if(ele%m==0 and ele%n==0):
            print(ele)

li=[10,20,2,3,4,5,6]
divisible(li)