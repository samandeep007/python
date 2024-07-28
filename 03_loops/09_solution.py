# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

# ```python
items = ["apple", "banana", "orange", "apple", "mango"]
# ```

def findDuplicate(myList):
    for i in range(0, len(myList)):
        if(myList.count(myList[i]) > 1):
            return myList[i]
    return -1;

print(findDuplicate(items))
