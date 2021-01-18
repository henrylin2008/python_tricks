# The collections module is a built-in module that implements specialized container data types providing alternatives
# to Python’s general purpose built-in containers. We've already gone over the basics: dict, list, set, and tuple.
#
# -Counters
# -OrderedDict
# -DefaultDict
# -ChainMap
# -NamedTuple
# -Deque
# -UserDict
# -UserList
# -UserString


# Counter
# Counter is a dict subclass which helps count hash-able objects. Inside of it elements are stored as dictionary keys
# and the counts of the objects are stored as the value.
#
#
# import collections
from collections import Counter

# Counter() with lists
l = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
Counter(l)
# Counter({1: 6, 2: 6, 3: 4, 32: 1, 12: 1, 21: 1, 223: 1})

# Counter with strings
Counter('aabsbsbsbhshhbbsbs')
# Counter({'b': 7, 's': 6, 'h': 3, 'a': 2})

# Counter with words in a sentence
s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
Counter(words)
# Counter({'word': 3, 'each': 3, 'times': 2, 'show': 1, 'this': 1, 'many': 1, 'in': 1, 'up': 1, 'How': 1, 'does': 1,
#          'sentence': 1})

# Methods with Counter(): most_common()
c = Counter(words)
c.most_common(2)    # (2) = most common items in c, parameter could be any number
# [('word', 3), ('each', 3)]

# Common patterns when using the Counter() object
# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts




# defaultdict
# defaultdict is a dictionary like object which provides all methods provided by dictionary but takes first argument
# (default_factory) as default data type for the dictionary. Using defaultdict is faster than doing the same using
# dict.set_default method.
# A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

d = {}
d['one']   # regular dict, return KeyError when no such item in the dictionary
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-22-07706fc5dc20> in <module>()
# ----> 1 d['one']
# KeyError: 'one'

from collections import defaultdict
d  = defaultdict(object)
d['one']
for item in d:
    print(item)
# one

# Can also initialize with default values:
d = defaultdict(lambda: 0)  # set the default value: 0
d['Two']
# 0


# OrderedDict
# An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
# For example a normal dictionary:

print('Normal dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v
# Normal dictionary:
# a A
# c C
# b B
# e E
# d D

# An Ordered Dictionary
print('OrderedDict:')
import collections
d = collections.OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)
# OrderedDict:
# a A
# b B
# c C
# d D
# e E

# Equality with an Ordered Dictionary
# A regular dict looks at its contents when testing for equality. An OrderedDict also considers the order the items
# were added.

# A normal Dictionary:
print('Dictionaries are equal? ')

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)
# Dictionaries are equal?
# True

# An Ordered Dictionary:
print('Dictionaries are equal? ')

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d2 = collections.OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)
# Dictionaries are equal?
# False




# namedtuple
# The standard tuple uses numerical indexes to access its members, for example:
t = (12,13,14)
t[0]
# 12

# For simple use cases, this is usually enough. On the other hand, remembering which index should be used for each value
# can lead to errors, especially if the tuple has a lot of fields and is constructed far from where it is used. A
# namedtuple assigns names, as well as the numerical index, to each member.
# Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function. The
# arguments are the name of the new class and a string containing the names of the elements.
# You can basically think of namedtuples as a very quick way of creating a new object/class type with some attribute
# fields.
#
# For example:

from collections import namedtuple
Dog = namedtuple('Dog','age breed name')    # namedtuple(typename, field_name['age', 'breed', 'name'])
sam = Dog(age=2,breed='Lab',name='Sammy')
frank = Dog(age=2,breed='Shepard',name="Frankie")

# We construct the namedtuple by first passing the object type name (Dog) and then passing a string with the variety of
# fields as a string with spaces between the field names. We can then call on the various attributes:
sam
# Dog(age=2, breed='Lab', name='Sammy')

sam.age
# 2

sam.breed
# 'Lab'

sam[0]
# 2

frank[2]
# Frankie