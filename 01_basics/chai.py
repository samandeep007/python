from hello_chai import chai

#Todo: Inner working of python
chai("Sandhu saab");

# >>> username.__contains__('S')
# PS G:\My projects\python\01_basics> python
# Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> myList = [123, "chai", 3.14]
# >>> myList
# [123, 'chai', 3.14]
# >>> len(myList)
# 3
# >>> dir(myList)
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# >>> myList.__contains__(3)
# False
# >>> myList.__iter__()
# <list_iterator object at 0x00000288D00E5750>
# >>> myList.reverse()
# >>>
# >>> myList
# [3.14, 'chai', 123]
# >>> myD = {'one': 'lemon tea', 'two': 'ginger tea', 'three': 'masala tea'}
# >>> dir(myD)
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# >>> myD['one']
# 'lemon tea'
# >>> myD.keys
# <built-in method keys of dict object at 0x00000288CFCF8CC0>
# >>> myD.keys()
# dict_keys(['one', 'two', 'three'])
# >>> myD.values()
# dict_values(['lemon tea', 'ginger tea', 'masala tea'])
# >>> dir(myD)
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# >>> myD.pop()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: pop expected at least 1 argument, got 0
# >>> myD.pop('three')
# 'masala tea'
# >>> myD
# {'one': 'lemon tea', 'two': 'ginger tea'}
# >>> myD.__contains__('ginger tea')
# False
# >>> myD.__contains__('two')
# True
# >>> myTup = (1,2,3,4)
# >>> myTup[0]
# 1
# >>> dir(myTup)
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
# >>> len(myTup)
# 4
# >>> sizeof(myTup)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'sizeof' is not defined
# >>> myTup.__sizeof__()
# 56
# >>> dir(myTup)
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
# >>> 5 > 4
# True
# >>> 5< 2
# False
# >>> 'delhi' == 'Delhi'
# False
# >>> 'delhi' == 'delhi'
# True
# >>> import sys
# >>> sys.getrefcount(10)
# 1000000023
# >>> sys.getrefcount(2313434)
# 3
# >>> sys.getrefcount(34342132434343434323434)
# 3
# >>> sys.getrefcount('hitesh')
# 3
# >>> sys.getrefcount('samandeep')
# 3
# >>> sys.getrefcount(1)
# 1000000210
# >>> sys.getrefcount(5)
# 1000000035
# >>> sys.getrefcount(7)
# 1000000024
# >>> sys.getrefcount(8)
# 1000000048
# >>> sys.getrefcount(9)
# 1000000024
# >>> sys.getrefcount(11)
# 1000000026
# >>> a = 3
# >>> a = 'chai aur code'
# >>> sys.getrefcount(3)
# 1000000052
# >>> a = 3.14
# >>>
# >>> a = 5
# >>> b = 2
# >>> a
# 5
# >>> b
# 2
# >>> a = a + 2
# >>> a
# 7
# >>> 
# >>> myListOne = [1,2,3,4,5]
# >>> myListTwo = myListOne
# >>> myListTwo
# [1, 2, 3, 4, 5]
# >>> myListOne[5] = 6
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list assignment index out of range
# >>> myListOne[4] = 6
# >>> myListTwo
# [1, 2, 3, 4, 6]
# >>> dir(myListTwo)
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# >>> myListTwo.__class__() 
# []
# >>> username = "Samandeep"
# >>> username.__class__()
# ''
# >>> username.__getstate__()
# >>> username.__getstate__
# <built-in method __getstate__ of str object at 0x00000288D00EC1B0>
# >>> username.__add__(" deep")
# 'Samandeep deep'
# >>> username
# 'Samandeep'
# >>> h1 = [1,2,3]
# >>> h2 = h1[:]
# >>> h1
# [1, 2, 3]
# >>> h2
# [1, 2, 3]
# >>> h1[0] = 4
# >>> h2
# [1, 2, 3]
# >>> h1
# [4, 2, 3]
# >>> h2
# [1, 2, 3]
# >>> import copu
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'copu'
# >>> import copy
# >>> h2 = copy.copy(h1)
# >>> h2
# [4, 2, 3]
# >>> h1[0] = 55;
# >>> h2
# [4, 2, 3]
# >>> h1
# [55, 2, 3]
# >>> n = [1,2,3]
# >>> m = n
# >>> m 
# [1, 2, 3]
# >>> m == n
# True
# >>> m is n
# True
# >>> n = [1,2,3]
# >>> m
# [1, 2, 3]
# >>> n
# [1, 2, 3]
# >>> m = [1,2,3]
# >>> m == n
# True
# >>> m  is n
# False
# >>> m is n
# False
# >>>  

# #