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
