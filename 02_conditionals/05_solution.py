# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

def suggestActivity(weather):
    weather = weather.title()
    if weather == "Sunny":
        return "Go for a walk"
    elif weather == "Rainy":
        return "Read a book"
    elif weather == "Snowy":
        return "Build a snowman"

weather = input("What's the weather today? : ")
print(suggestActivity(weather))