# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
np=int(input('Enter No of Passengers :'))
mp=0
ticket_cost=1000
temp=ticket_cost
age=1
sen_cost=0
child_cost=0
teen=0
total_amount=0
    #tp=ticket_cost*i
    #print(i,'total ticket=',tp)
for i in range(np):
    age=int(input('Enter Age :'))
    if(age<12):
        child_cost=ticket_cost*30/100
        child_cost=ticket_cost-child_cost
    elif(age>59):
        sen_cost=ticket_cost*50/100
        sen_cost=ticket_cost-sen_cost
    else:
        teen=1000

total_amount=child_cost+sen_cost+teen
print(f'Total Cost to Pay={total_amount}')




