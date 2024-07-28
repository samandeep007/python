# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
def classifyAge(age):
    if age < 13:
        return "Child"
    elif age >= 13 and age <=19:
        return "Teenager"
    elif age >= 20 and age <= 59:
        return "Adult"
    else:
        return "Senior"
    

age = int(input("Enter your age: "))
print(classifyAge(age))




