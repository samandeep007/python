# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

def getGrade(score):
    
    if score >= 101:
        return "Please verify your grade again"
    
    if score < 60:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    else:
        return 'A'
    
score = int(input("Enter your score: "))
print(getGrade(score))