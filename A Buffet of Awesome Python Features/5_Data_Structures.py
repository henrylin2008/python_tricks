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






