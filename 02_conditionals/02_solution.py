# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
import datetime
def getTicketPrice(age):
    today = datetime.datetime.today()
    ticketPrice = 0
    if age>=18:
       ticketPrice = 12
    else:
        ticketPrice = 8
    if(today.weekday() == 3):
        ticketPrice = ticketPrice - 2
    return ticketPrice


age = int(input("Enter your age: "))
print("The ticket costs $" + str(getTicketPrice(age)))