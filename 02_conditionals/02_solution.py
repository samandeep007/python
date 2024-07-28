# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

def getTicketPrice(age, day):
    ticketPrice = 0
    if age>=18:
       ticketPrice = 12
    else:
        ticketPrice = 8
    if(day.lower() == "wednesday"):
        ticketPrice = ticketPrice - 2
    return ticketPrice


age = int(input("Enter your age: "))
day = input("Enter the day today: ")
print("The ticket costs $" + str(getTicketPrice(age, day)))