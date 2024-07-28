# >>> tea_types = ("Black", "Green", "Lemon")

# >>> tea_types[0]
# 'Black'
# >>> tea_types[-1]
# 'Lemon'
# >>> tea_types[:1]
# ('Black',)

# >>> tea_types[0] = "Oolong" --> Trying to change the value of a tuple is not allowed.
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment


# >>> print(len(tea_types))
# 3
# >>> print(tea_types[:2])
# ('Black', 'Green')

# >>> more_tea = ("Herbal", "Oolong", "Earl Grey")
# >>> all_tea = more_tea + tea_types
# >>> print(all_tea)
# ('Herbal', 'Oolong', 'Earl Grey', 'Black', 'Green', 'Lemon')