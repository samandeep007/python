# 4. Reverse a String
# </summary>
# Problem: Reverse a string using a loop.

def getReversedString(str):
    for i in range(-1, -len(str)-1, -1):
        print(str[i], end="")
        
input = input("Enter a string: ")
getReversedString(input)