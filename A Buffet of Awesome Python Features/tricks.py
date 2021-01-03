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

# Counting items
from collections import defaultdict

dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]
dd = defaultdict(int)
for department, _ in dep:
    dd[department] += 1
dd
# defaultdict(<class 'int'>, {'Sales': 2, 'Accounting': 1, 'Marketing': 2})

# Accumulating Values
incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00)]

from collections import defaultdict

dd = defaultdict(float)
for product, income in incomes:
    dd[product] += income

for product, income in dd.items():
    print(f'Total income for {product}: ${income:,.2f}')
# Total income for Books: $3,970.00
# Total income for Tutorials: $1,940.00
# Total income for Courses: $7,680.00


# Collections.Counter
# return 0 for non-existing item
from collections import Counter

c = Counter(cats=4, dogs=3)
print(c['pets'])
# 0

print(list(c.elements()))  # print list of elements
['cats', 'cats', 'cats', 'cats', 'dogs', 'dogs', 'dogs']

Counter('mississippi').most_common(2)  # most (first 2) common items
[('i', 4), ('s', 4)]

c = Counter(a=4, b=3, c=2, d=0)
d = ['a', 'b', 'b', 'c', 'c']
c.subtract(d)  # subtraction: items in c - d
c
# Counter({'a': 3, 'b': 1, 'c': 0, 'd': 0})
c.update(d)  # adding c and d
c
# Counter({'a': 4, 'b': 3, 'c': 2, 'd': 0})
c.clear()  # clear out c
c
# Counter()

c = Counter(a=4, b=3, c=2, d=0)
d = Counter(['a', 'b', 'b', 'c', 'c'])
c + d  # sum up c and d, item with 0 not showing
# Counter({'a': 5, 'b': 5, 'c': 4})
c - d  # subtract d from c
# Counter({'a': 3, 'b': 1})
c & d  # intersection of c & d, minimum item from both lists
# Counter({'b': 2, 'c': 2, 'a': 1})
c | d  # union of c & d, max item from both list
# Counter({'a': 4, 'b': 3, 'c': 2})


# collections deque
from collections import deque

d = deque('hello')
d.append(4)  # deque(['h', 'e', 'l', 'l', 'o', 4])
d.appendleft(5)  # deque([5, 'h', 'e', 'l', 'l', 'o', 4])
d.pop()  # deque([5, 'h', 'e', 'l', 'l', 'o'])
d.popleft()  # deque(['h', 'e', 'l', 'l', 'o'])
d.clear()  # empty the deque object, deque([])
d.extend('456')  # add all of the items  from the passed iterable data type or collection to the end of the deque
# to the end of the deque. deque(['4', '5', '6'])
d.extend('hello')  # deque(['4', '5', '6', 'h', 'e', 'l', 'l', 'o'])
d.extendleft('19')  # deque(['9', '1', '4', '5', '6', 'h', 'e', 'l', 'l', 'o'])
d = deque("hello")  # rotate the deck by that many positions. Takes and iterable
d.rotate(1)
print(d)  # prints deque(["o", "h", "e", "l", "l"])
d.rotate(-2)
print(d)  # prints deque(["e", "l", "l", "o", "h"])

# timeit.timeit
import timeit

timeit.timeit('"-".join(str(n) for n in range(100))',
              number=10000)

0.3412662749997253


# timeit.timeit(stmt, setup, timer, number)
# stmt - which is the statement you want to measure; it defaults to ‘pass’.
# setup - which is the code that you run before running the stmt; it defaults to ‘pass’.
#         We generally use this to import the required modules for our code.
# timer - which is a timeit.Timer object; it usually has a sensible default value so you don’t have to worry about it.
# number - which is the number of executions you’d like to run the stmt.


# Functions are first-class citizens in Python:
# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.

def myfunc(a, b):
    return a + b


funcs = [myfunc]
funcs[0]
# <function myfunc at 0x107012230>
funcs[0](2, 3)
# 5
