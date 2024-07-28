# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

def getModeOfTransportation(distance):
    if distance < 3:
        return "Walk"
    elif distance <= 15:
        return "Bike"
    else:
        return "Car"

distance = int(input("Enter the distance: "))
print("You should take a " + str(getModeOfTransportation(distance)))