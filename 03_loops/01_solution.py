# Problem: Given a list of numbers, count how many are positive.

# ```python
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# ```

count = 0
for number in numbers:
    if number > 0:
        count+=1

print(count)
        