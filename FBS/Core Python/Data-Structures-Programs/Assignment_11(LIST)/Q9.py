# Write a program to create three lists of numbers, their squares and cubes

def cube(li):
    cubee=[]
    square=[]
    for ele in li[:]:
        cubee.append(ele ** 3)
        square.append(ele ** 2)
    print(cubee)
    print(square)

li=[3,2,4,5]
cube(li)