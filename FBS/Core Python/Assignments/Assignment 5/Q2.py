# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

stu=int(input('Enter No of students='))
for i in range(1,stu+1):
    all_avg=0
    mark1=int(input('Enter Mark for sub 1 :'))
    mark2=int(input('Enter Mark for sub 2 :'))
    mark3=int(input('Enter Mark for sub 3 :'))
    mark4=int(input('Enter Mark for sub 4 :'))
    mark5=int(input('Enter Mark for sub 5 :'))
    avg=0
    avg=(mark1+mark2+mark3+mark4+mark5)/5
    print(f'Average={avg}')
    all_avg=avg/stu
print(f'All stud avg={all_avg}')






