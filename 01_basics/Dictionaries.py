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


# >>> for key, value in chai_types.items(): --> items() will return a list of tuples where each tuple contains a key-value pair.
# ...     print("{} chai has {} taste".format(key, value))
# ...
# Masala chai has Spicy taste
# Ginger chai has Zesty taste
# Green chai has Fresh taste


# >>> for chai in chai_types: --> This will print all keys. In lists, if we iterate over a list, we get values.
# ...     print(chai)
# ...
# Masala
# Ginger
# Green


# >>> for chai in chai_types: --> This will print all values.
# ...     print(chai_types[chai])
# ...
# Spicy
# Zesty
# Fresh


# >>> for key, value in chai_types.items():
# ...     print("{} chai has {} taste".format(key, value))
# ...
# Masala chai has Spicy taste
# Ginger chai has Zesty taste
# Green chai has Fresh taste


# >>> if "Masala" in chai_types:
# ...     print("We have Masala Chai")
# ...
# We have Masala Chai


# >>> print(len(chai_types))
# 3

# >>> chai_types["Earl Grey"] = "Citrus"
# >>> print(chai_types)
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}

# >>> chai_types.pop("Ginger") #Here you have to provide key  
# 'Zesty'

# >>> chai_types.popitem()
# ('Earl Grey', 'Citrus')
# >>> print(chai_types)
# {'Masala': 'Spicy', 'Green': 'Fresh'}

# >>> del chai_types["Green"] --> del() function deletes the specified key-value pair from the dictionary. Deletes the reference from memory.
# >>> chai_types
# {'Masala': 'Spicy'}

# >>> chai_types_copy = chai_types.copy()

# >>> tea_shop = {
# ... "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
# ... "Tea": {"Green": "Mild", "Black": "Strong"}
# ... }

# >>> tea_shop["chai"]
# {'Masala': 'Spicy', 'Ginger': 'Zesty'}
# >>> tea_shop["chai"]["Ginger"]
# 'Zesty'

# Dictionary comprehension:
# >>> squared_nums = {x:x**2 for x in range(1,6)}
# >>> print(squared_nums)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# >>> squared_nums.clear()
# >>> print(squared_nums)
# {}

# >>> new_dict = dict.fromkeys(keys, default_value)
# >>> print(new_dict)
# {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}

