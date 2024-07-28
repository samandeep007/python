# 6. Factorial Calculator
# </summary>
# Problem: Compute the factorial of a number using a while loop.

def getFactorial(num):
    factorial = 1
    i = num
    while(i > 0):
        factorial *= i
        i-=1
    return factorial

num = int(input("Enter a number: "))
print(getFactorial(num))
         