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