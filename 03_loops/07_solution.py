# 7. Validate Input
# </summary>
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

num = int(input("Please enter a number: "))
while(not( num>=1 and num <= 10)):
    num = int(input("Please enter a number: "))