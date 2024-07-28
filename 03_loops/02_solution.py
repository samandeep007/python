# 2. Sum of Even Numbers
# </summary>
# Problem: Calculate the sum of even numbers up to a given number n.
def sumEvenNumbers(upperLimit):
    sum = 0
    for num in range(0, upperLimit+1, 2):
        sum += num
    return sum

upperLimit = int(input('Enter a number: '))
print(sumEvenNumbers(upperLimit))

