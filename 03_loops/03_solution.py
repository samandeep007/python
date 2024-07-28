# 3. Multiplication Table Printer
# </summary>
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

def getMultiplicationTable(num):
    for i in range(1, 11):
        if(i == 5):
            continue
        else:
            print("{} x {} = {}".format(num, i, num*i))
            
            
num = int(input("Enter the number: "))
getMultiplicationTable(num)