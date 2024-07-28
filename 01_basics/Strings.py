# >>> # '' or " " or """ """ --> String literals in Python are enclosed in either single quotes, double quotes, or triple quotes. Triple quotes can span multiple lines and are useful when you want to include a lot of text
# >>> chai = "Lemon Chai"
# >>> print(chai)
# Lemon Chai


# >>> chai = "Masala chai"
# >>> firstChar = chai[0]
# >>> print(firstChar)  
# M
# >>> chai
# 'Masala chai'


# >>> slice_chai = chai[0:6] # last index is not included
# >>> print(slice_chai)
# Masala

# >>> num_list = "0123456789"
# >>> num_list[:] 
# '0123456789'
# >>> num_list[3:] 
# '3456789'
# >>> num_list[:7] # first 7 characters
# '0123456'
# >>> num_list[0:7:2] # Step size of 2
# '0246'
# >>> num_list[::3] # Step size of 3
# '0369'


# >>> print(chai.lower())
# masala chai
# >>> print(chai.upper())
# MASALA CHAI
# >>> print(chai.title())
# Masala Chai
# >>> print(chai.strip()) 
# Masala Chai
# >>> chai = "Lemon Chai"
# >>> print(chai.replace("Lemon", "Ginger"))
# Ginger Chai
# >>> chai = "Lemon, Ginger, Masala, Mint"
# >>> print(chai.split(', '))
# ['Lemon', 'Ginger', 'Masala', 'Mint']


