# How to sort a Python dict by value (== get a representation sorted by value)
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sorted(xs.items(), key=lambda x: x[1])
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
# Or:
import operator

sorted(xs.items(), key=operator.itemgetter(1))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]


# Different ways to test multiple flags at once in Python
x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    print('passed')
# passed
if 1 in (x, y, z):
    print('passed')
# passed

# These only test for truthiness:
if x or y or z:
    print('passed')
# passed
if any((x, y, z)):
    print('passed')

# How to merge two dictionaries in Python 3.5+
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}  # duplicate item (b) from y overwrites same item in x
z
# {'c': 4, 'a': 1, 'b': 3}

# In Python 2.x you could
# use this:
z = dict(x, **y)
z
# {'a': 1, 'c': 4, 'b': 3}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting
# duplicates from left to right.
#
# See: https://www.youtube.com/watch?v=Duexw08KaC8

# Copying List
# a fast way to make a shallow copy of a list
a  # [1,2,3,4,5]
b = a
b[0] = 10
# both a and b will be [10,2,3,4,5]

b = a[:]
b[0] = 10
# only b will change to [10,2,3,4,5]

# copy list by typecasting method
a = [1, 2, 3, 4, 5]
print(list(a))

# using the list.copy() method (python3 only)
a = [1, 2, 3, 4, 5]
print(a.copy())

# copy nested lists using copy.deepcopy
from copy import deepcopy

l = [[1, 2], [3, 4]]
l2 = deepcopy(l)
print(l2)  # [[1,2], [3,4]]

# Dictionary Get
# Returning None or default value, when key is not in dict
d = {'a': 1, 'b': 2}
print(d.get('c', 3))  # 3 is default value, returning 3

# Sort Dictionary by Value
# Sort a dictionary by its values with the built-in sorted() function and a 'key' argument.
d = {'a': 10, 'b': 12, 'c': 7, 'f': 2, 'e': 8, 'd': 3}
print(sorted(d.items(), key=lambda x: x[1]))
# [('f', 2), ('d', 3), ('c', 7), ('e', 8), ('a', 10), ('b', 12)]

# Sort using operator.itemgetter as the sort key instead of a lambda
from operator import itemgetter

print(sorted(d.items(), key=itemgetter(1)))

# sort dict keys by value
print(sorted(d, key=d.get))
# ['f', 'd', 'c', 'e', 'a', 'b']

# Find min and max index in List
lst = [40, 10, 20, 30]


def minIndex(lst):
    return min(range(len(lst)), key=lst.__getitem__)  # 1


def maxIndex(lst):
    return max(range(len(lst)), key=lst.__getitem__)  # 0


# remove duplicates from a list
items = [2, 2, 3, 3, 1]
items2 = list(set(items))
print(items2)  # [1, 2, 3]

# remove dupls and keep order
from collections import OrderedDict

items = ["foo", "bar", "bar", "foo"]
print(list(OrderedDict.fromkeys(items).keys()))  # ['foo', 'bar']

# The get() method on dicts and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}


def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")


greeting(382)
# "Hi Alice!"

greeting(333333)
# "Hi there!"


# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than defining a class manually:
from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
my_car.color
# 'red'
my_car.mileage
# 3812.4

# We get a nice string repr for free:
my_car
# Car(color='red' , mileage=3812.4)

# Like tuples, namedtuples are immutable:
my_car.color = 'blue'


# AttributeError: "can't set attribute"


# Function argument unpacking
def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


# unpack tuple
tuple_vec = (1, 0, 1)
print_vector(*tuple_vec)
# <1, 0, 1>

# unpack dictionary
dict_vec = {'x': 1, 'y': 0, 'z': 1}
print_vector(**dict_vec)
# <1, 0, 1>
print_vector(*dict_vec)  # unpacking the keys
# <x, y, z>


# Using json.dumps() to pretty-print dicts
# The standard string repr for dicts is hard to read:
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
my_mapping
# {'b': 42, 'c': 12648430. 'a': 23}  # 😞

# The "json" module can do a much better job:
import json
print(json.dumps(my_mapping, indent=4, sort_keys=True))
# {
#     "a": 23,
#     "b": 42,
#     "c": 12648430
# }

# loops
my_items = ['a', 'b', 'c']
for i in range(len(my_items)):
    print(my_items[i])
# a
# b
# c
for i in my_items:
    print(i)
# a
# b
# c
for i, item in enumerate(items):
    print(i, item)
# 0 a
# 1 b
# 2 c

# Defaultdict vs regular dict
# The main difference between defaultdict and dict is that when you try to access or
# modify a key that’s not present in the dictionary, a default value is automatically given to that key. In order to
# provide this functionality, the Python defaultdict type does two things:
# 1. It overrides .__missing__().
# 2. It adds .default_factory, a writable instance variable that needs to be provided at the time of instantiation.
# The instance variable .default_factory will hold the first argument passed into defaultdict.__init__(). This argument
# can take a valid Python callable or None. If a callable is provided, then it’ll automatically be called by defaultdict
# whenever you try to access or modify the value associated with a missing key.
from collections import defaultdict
dd = defaultdict(list)
dd['missing_key']
# []
dd
# defaultdict(<class 'list'>, {'missing_key': []})
# using a defaultdict to handle missing keys can be faster than using dict.setdefault()

# guidelines when to use a defaultdict rather than a regular dict
# 1.If your code is heavily base on dictionaries and you’re dealing with missing keys all the time, then you should
# consider using a defaultdict rather than a regular dict.
# 2.If your dictionary items need to be initialized with a constant default value, then you should consider using a
# defaultdict instead of a dict.
# 3.If your code relies on dictionaries for aggregating, accumulating, counting, or grouping values, and performance is
# a concern, then you should consider using a defaultdict.

# grouping defaultdict
dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]

from collections import defaultdict

dep_dd = defaultdict(list)
for department, employee in dep:
    dep_dd[department].append(employee)

dep_dd
# defaultdict(<class 'list'>, {'Sales': ['John Doe', 'Martin Smith'],
#                              'Accounting' : ['Jane Doe'],
#                              'Marketing': ['Elizabeth Smith', 'Adam Doe']})