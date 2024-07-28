# 5. Find the First Non-Repeated Character
# </summary>
# Problem: Given a string, find the first non-repeated character.

def getFirstNonRepeatedChar(s):
    for char in s:
        if s.count(char) == 1:
            return char

string = input("Enter a string: ")
print(getFirstNonRepeatedChar(string))