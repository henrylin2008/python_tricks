# 5.1 Dictionaries, Maps, and Hashtables
# Dictionary: O(1) time complexity for lookup, insert, update, and delete operations in the average case
import collections

d = collections.OrderedDict(one=1, two=2, three=3)
# d: OrderedDict([('one', 1), ('two', 2), ('three', 3)])
d['four'] = 4
# d: OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
d.keys()
# odict_keys(['one', 'two', 'three', 'four'])

# The defaultdict class is another dictionary subclass that accepts a callable in its constructor whose return value
# will be used if a requested key cannot be found.
from collections import defaultdict

dd = defaultdict(list)

# Accessing a missing key creates it and
# initializes it using the default factory,
# i.e. list() in this example:
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')

dd['dogs']
# ['Rufus', 'Kathrin', 'Mr Sniffles']

# The collections.ChainMap data structure groups multiple dictionaries into a single mapping. Lookups search the
# underlying mappings one by one until a key is found. Insertions, updates, and deletions only affect the first
# mapping added to the chain.
from collections import ChainMap

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = ChainMap(dict1, dict2)
# chain: ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})
#
# # ChainMap searches each collection in the chain
# # from left to right until it finds the key (or fails)
chain['three']
# 3
chain['one']
# 1
chain['missing']
# KeyError: 'missing'
#
# MappingProxyType is a wrapper around a standard dictionary that provides a read-only view into the wrapped
# dictionary’s data.
# Using MappingProxyType allows you to return a dictionary carrying internal state from a class or module, while
# discouraging write access to this object.
from types import MappingProxyType

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

# The proxy is read-only:
read_only['one']
1
read_only['one'] = 23
# TypeError:
# "'mappingproxy' object does not support item assignment"

# Updates to the original are reflected in the proxy:
writable['one'] = 42
read_only
# mappingproxy({'one': 42, 'two': 2})

# Key Takeaways:
# -The built-in dict type will be “good enough” most of the time.
# -Specialized implementations, like read-only or ordered dicts, are available in the Python standard library.


# 5.2 Array
# Arrays consist of fixed-size data records that allow each element to be efficiently located based on its index.
# It’s very fast to look up an element contained in an array given the element’s index. A proper array
# implementation guarantees a constant O(1) access time for this case.

# List: implemented as dynamic arrays behind the scenes
# ex: arr = ['one', 'two', 'three']

# Tuple: objects are immutable. This means elements can’t be added or removed dynamically—all elements in a
# tuple must be defined at creation time.
# ex: arr = 'one', 'two', 'three'

# array.array: (single data type)
# Arrays created with the array.array class are mutable and behave similarly to lists, except for one
# important difference—they are “typed arrays” constrained to a single data type.
import array

arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
# arr[1]: 1.5

# str: (single data type)
# String objects are space-efficient because they’re tightly packed and they specialize in a single data type.
# - strings are immutable
# - Not support item assignment, item deletino
# ex: arr = 'abcd'
# Strings are immutable:
# >>> arr[1] = 'e'
# TypeError:
# "'str' object does not support item assignment"

# bytes: immutable arrays of single bytes
# Bytes objects are immutable sequences of single bytes (integers in the range of 0 <= x <= 255).
# - immutable
# - Does not support item assignment, item deletion
# ex:
# >>> arr = bytes((0, 1, 2, 3))
# >>> arr[1]
# 1

# bytearray
# The bytearray type is a mutable sequence of integers in the range 0 <= x <= 255.
# - mutable
# - overwrite elements, remove elements, or add new ones s
# >>> arr = bytearray((0, 1, 2, 3))
# >>> arr[1]
# 1

# Key Takeaways
# You need to store arbitrary objects, potentially with mixed data types?
# Use a list or a tuple, depending on whether you want an immutable data structure or not.
#
# You have numeric (integer or floating point) data and tight packing and performance is important?
# Try out array.array and see if it does everything you need. Also, consider going beyond the standard library and try
# out packages like NumPy or Pandas.
#
# You have textual data represented as Unicode characters?
# Use Python’s built-in str. If you need a “mutable string,” use a list of characters.
#
# You want to store a contiguous block of bytes?
# Use the immutable bytes type, or bytearray if you need a mutable data structure.

# 5.3 Records, Structs, and Data Transfer Objects
# Dictionaries:
# Dictionaries are also often called maps or associative arrays and allow for the efficient lookup, insertion, and
# deletion of any object associated with a given key.
# there’s little protection against misspelled field names, as fields can be added and removed freely at any time.
#
# ex:
# car1 = {
#     'color': 'red',
#     'mileage': 3812.4,
#     'automatic': True,
# }
#
# tuple
# -Immutable
# - Take up slightly less memory than lists in CPython

# Custom class
# Classes allow you to define reusable “blueprints” for data objects to ensure each object provides the same set of
# fields.
# - a great option whenever you’d like to add business logic and behavior to your record objects using methods.

# Data objects
# The namedtuple class provides an extension of the build-in tuple data type
# Namedtuples are immutable
from collections import namedtuple

Car = namedtuple('Car', 'color mileage automatic')
car1 = Car('red', 3812.4, True)
car1
# Car(color='red', mileage=3812.4, automatic=True)

# typing.NamedTuple - Improved Namedtuples
from typing import NamedTuple

class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool


car1 = Car('red', 3812.4, True)

# struct.Struct - Serialized C Structs
# The struct.Struct class converts between Python values and C structs serialized into Python bytes objects.
from struct import Struct
MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)

# All you get is a blob of data:
data
# b'\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00(B'

# Data blobs can be unpacked again:
MyStruct.unpack(data)
# (23, False, 42.0)

# types.SimpleNamespace - Fancy Attribute Access
# it provides attribute access to its namespace.
# This means SimpleNamespace instances expose all of their keys as class attributes. This means you can use obj.key
# “dotted” attribute access instead of the obj['key'] square-brackets indexing syntax that’s used by regular dicts.
#
from types import SimpleNamespace
car1 = SimpleNamespace(color='red',
                       mileage=3812.4,
                       automatic=True)

# The default repr:
>>> car1
# namespace(automatic=True, color='red', mileage=385.3)

# Instances support attribute access and are mutable:
car1.mileage = 12
car1.windshield = 'broken'
del car1.automatic
car1
# namespace(color='red', mileage=12, windshield='broken')

# Key Takeaways
# -You only have a few (2-3) fields: Using a plain tuple object may be okay if the field order is easy to remember or
# field names are superfluous. For example, think of an (x, y, z) point in 3D space.
# -You need immutable fields: In this case, plain tuples, collections.namedtuple, and typing.NamedTuple would all make
# good options for implementing this type of data object.
# -You need to lock down field names to avoid typos: collections.namedtuple and typing.NamedTuple are your friends here.
# -You want to keep things simple: A plain dictionary object might be a good choice due to the convenient syntax that
#  closely resembles JSON.
# -You need full control over your data structure: It’s time to write a custom class with @property setters and getters.
# -You need to add behavior (methods) to the object: You should write a custom class, either from scratch or by
#  extending collections.namedtuple or typing.NamedTuple.
# -You need to pack data tightly to serialize it to disk or to send it over the network: Time to read up on
#  struct.Struct because this is a great use case for it.

# 5.4 Sets and Multisets
# A set is an unordered collection of objects that does not allow duplicate elements.
# In a “proper” set implementation, membership tests are expected to run in fast O(1) time. Union, intersection,
# difference, and subset operations should take O(n) time on average.
# The set type is mutable and allows for the dynamic insertion and deletion of elements.
#
# vowels = {'a', 'e', 'i', 'o', 'u'}
# vowels.add('x')
# vowels:
# {'i', 'a', 'u', 'o', 'x', 'e'}

# frozenset - Immutable sets
# The frozenset class implements an immutable version of set that cannot be changed after it has been constructed.
# >>> vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
# >>> vowels.add('p')
# AttributeError:
# "'frozenset' object has no attribute 'add'"
#
# Frozensets are hashable and can be used as dictionary keys:
# >>> d = { frozenset({1, 2, 3}): 'hello' }
# >>> d[frozenset({1, 2, 3})]
# 'hello'


# collections.Counter - Multisets
# The collections.Counter class in the Python standard library implements a multiset (or bag) type that allows elements
# in the set to have more than one occurrence.
# This is useful if you need to keep track of not only if an element is part of a set, but also how many times it is
# included in the set:
#
from collections import Counter
inventory = Counter()
#
loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
inventory
# Counter({'bread': 3, 'sword': 1})
#
more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot)
inventory
# Counter({'bread': 3, 'sword': 2, 'apple': 1})

len(inventory)
# 3  # Unique elements
sum(inventory.values())
# 6 # Total no. of elements

# Key Takeaways:
# -Use the built-in set type when looking for a mutable set.
# -frozenset objects are hashable and can be used as dictionary or set keys.
# -collections.Counter implements multiset or “bag” data structures.

# 5.5 Stacks (LIFOs)
# A stack is a collection of objects that supports fast last-in, first-out (LIFO) semantics for inserts and deletes.
# Insert: push: O(1) time, append()
# Delete: pop: O(1) time, pop()
s = []
s.append('eat')
s.append('sleep')
s.append('code')

s
# ['eat', 'sleep', 'code']

s.pop()
# 'code'
s.pop()
# 'sleep'
s.pop()
# 'eat'

s.pop()
# IndexError: "pop from empty list"

# collections.deque - Fast & robust stacks
# The deque class implements a double-ended queue that supports adding and removing elements from either end in O(1)
# time (non-amortized).
# pop(), append(): O(1) time
# Randomly access elements in the middle of a stack: O(n)
from collections import deque
s = deque()
s.append('eat')
s.append('sleep')
s.append('code')

s
# deque(['eat', 'sleep', 'code'])

s.pop()
# 'code'
s.pop()
# 'sleep'
s.pop()
# 'eat'

s.pop()
# IndexError: "pop from an empty deque"

# queue.LifoQueue – Locking Semantics for Parallel Computing
from queue import LifoQueue
s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('code')

s
# <queue.LifoQueue object at 0x108298dd8>

s.get()
# 'code'
s.get()
# 'sleep'
s.get()
# 'eat'

s.get_nowait()
# queue.Empty

s.get()
# Blocks / waits forever...

# collections.deque is an excellent choice for implementing a stack (LIFO queue) in Python.

# Key Takeaways:
# -collections.deque provides a safe and fast general-purpose stack implementation.
# -The built-in list type can be used as a stack, but be careful to only append and remove items with append() and pop()
#  in order to avoid slow performance.


#
