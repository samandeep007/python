# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
import datetime
def getTicketPrice(age):
    today = datetime.datetime.today()
    price = 12 if age >= 18 else 8
    if(today.weekday() == 3):
       price -= 2
    return price


age = int(input("Enter your age: "))
print("The ticket costs $" + str(getTicketPrice(age)))