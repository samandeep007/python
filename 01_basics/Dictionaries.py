# >>> chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

# Ways to access elements:
# >>> chai_types["Masala"]
# 'Spicy'
# >>> chai_types.get("Masala")
# 'Spicy'


# >>> chai_types.get("Lemon")
# >>> chai_types["Lemon"]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'Lemon'

# >>> chai_types["Green"] = "Fresh" --> This will add a new key-value pair if the key does not exist, otherwise it will
# >>> print(chai_types)                 
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}