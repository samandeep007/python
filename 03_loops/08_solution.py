# 8. Prime Number Checker
# </summary>
# Problem: Check if a number is prime.

def checkPrime(num):
    if num <= 1:
        return False 
    if num == 2:
            return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print("The number is " + ("" if checkPrime(num) == True else "not ") + "prime")