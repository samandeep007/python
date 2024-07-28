# >>> tea_varieties = ['Black', 'Green', 'Oolong', 'White']
# >>> print(tea_varieties)
# ['Black', 'Green', 'Oolong', 'White']

# >>> print(tea_varieties[0])
# Black
# >>> print(tea_varieties[-1])
# White
# >>> print(tea_varieties[0:2])
# ['Black', 'Green']
# >>> print(tea_varieties[2:])
# ['Oolong', 'White']

# >>> tea_varieties[3] = 'herbal'
# >>> print(tea_varieties)
# ['Black', 'Green', 'Oolong', 'herbal']


# >>> tea_varieties[1:2]
# ['Green']

# >>> tea_varieties[1:2] = "Lemon" --> Lemon will be treated as a list
# >>> print(tea_varieties)
# ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'herbal']

# >>> tea_varieties[1:2] = ["Lemon"]
# >>> print(tea_varieties)
# ['Black', 'Lemon', 'Oolong', 'White']

# >>> tea_varieties[1:3]
# ['Lemon', 'Oolong']
# >>> tea_varieties[1:3] = ['Green', 'Masala']
# >>> print(tea_varieties)
# ['Black', 'Green', 'Masala', 'White']

# >>> tea_varieties[1:1] --> will insert at the first index
# []
# >>> tea_varieties[1:1] = ["test", "test"]
# >>> print(tea_varieties)
# ['Black', 'test', 'test', 'Green', 'Masala', 'White']

# >>> tea_varieties[1:3] = [] --> will remove the elements from 1 to 2 index           
# >>> print(tea_varieties)    
# ['Black', 'Green', 'Masala', 'White']

# Why do we need it?
# >>> tea_varieties[1] = ['Saman', 'Sandhu']
# >>> print(tea_varieties)
# ['Black', ['Saman', 'Sandhu'], 'Masala', 'White']

# >>> for variety in tea_varieties:  
# ...     print(variety)
# ... 
# Black
# Green
# Oolong
# White

# >>> for variety in tea_varieties: 
# ...     print(variety, end="-") --> This will print all elements separated by "-". By default, print() function adds a newline character at the end.
# ...
# Black-Green-Oolong-White->>>

# >>> if "Oolong" in tea_varieties: 
# ...     print("I have Oolong tea")
# ...
# I have Oolong tea

# >>> tea_varieties.append("Ginger")
# >>> print(tea_varieties)
# ['Black', 'Green', 'Oolong', 'White', 'Ginger']
# >>> if "Ginger" in tea_varieties:   
# ...     print("We have Ginger tea")
# ...
# We have Ginger tea

# >>> tea_varieties.pop() --> This will remove the last element from the list
# 'Ginger'

# >>> tea_varieties.remove("Green") --> This will remove the first occurrence of the specified element from the list
# >>> print(tea_varieties)
# ['Black', 'Oolong', 'White']

# >>> tea_varieties.insert(1, "green") --> This will insert the specified element at the specified index
# >>> print(tea_varieties)
# ['Black', 'green', 'Oolong', 'White']

# >>> tea_varieties_copy = tea_varieties.copy()
# >>> print(tea_varieties_copy)
# ['Black', 'green', 'Oolong', 'White']
# >>> print(tea_varieties is tea_varieties_copy)
# False

# >>> tea_varieties_copy.append("Lemon")
# >>> print(tea_varieties) 
# ['Black', 'green', 'Oolong', 'White']
# >>> print(tea_varieties_copy)
# ['Black', 'green', 'Oolong', 'White', 'Lemon']


# List comprehension:
# >>> squared_nums = [x**2 for x in range(10)] --> This will create a new list with squares of numbers from 0 to 9. Range starts from 0 and goes up to but not including 10.
# >>> print(squared_nums)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# >>> y = range(10)       
# >>> for i in y:
# ...     print(i)
# ...
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


