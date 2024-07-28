# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

def checkBananaRipeness(color):
    color = color.lower()
    if color == "green":
        return "Unripe"
    elif color == "yellow":
        return "Ripe"
    elif color == "brown":
        return "Overripe"

color = input("Enter the color of the banana: ")
print("The fruit is " + checkBananaRipeness(color))
        