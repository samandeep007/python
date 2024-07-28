# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

def isLeapYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = int(input("Enter the year: "))
print("The year is " + ("a " if isLeapYear(year) == True else "not a ") + "leap year")