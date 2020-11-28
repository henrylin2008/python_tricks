name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}


# 7.1: Dictionary Default values
# Easier to ask for forgiveness than permission (EAFP), try & except to catch KeyError
def greeting(userid):
    try:
        return 'Hi %s!' % name_for_userid[userid]
    except KeyError:
        return 'Hi there'


# >>> greeting(382)
# 'Hi Alice!'
#
# >>> greeting(33333333)
# 'Hi there!'


# When get() is called, it checks if the given key exists in the dictionary. If it does, the value for the key is
# returned. If it does not exist, then the value of the default parameter is returned instead.
def greeting(userid):
    return 'Hi %s!' % name_for_userid.get(userid, 'there')


# 7.2: Sorting Dictionary
xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}

# To compare two tuples, Python compares the items stored at index zero. If they differ, this defines the outcome of
# the comparison. If they’re equal, the next two items at index one are compared, and so on.ßß
sorted(xs.items())
# [('a', 4), ('b', 3), ('c', 2), ('d', 1)]ß

# get a sorted representation of a dictionary based on its values (second element)
sorted(xs.items(), key=lambda x: x[1])
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
# sorted(xs.items(), key=lambda x: abs(x[1])), get absolute value of second item

# using operator; ex: operator.itemgetter, operator.attrgetter
import operator

sorted(xs.items(), key=operator.itemgetter(1))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]


# reverse the sort order so that larger values go first
sorted(xs.items(),
       key=lambda x: x[1],
       reverse=True)


# [('a', 4), ('b', 3), ('c', 2), ('d', 1)]


# 7.3 Emulating Switch/Case
# Store function in a list
def myfunc(a, b):
    return a + b


funcs = [myfunc]
funcs[0]
# <function myfunc at 0x107012230>

funcs[0](2, 3)
5

# define a dictionary that maps lookup keys for the input conditions to functions that will carry out the intended
# operations:
func_dict = {
    'cond_a': handle_a,
    'cond_b': handle_b
}

# dictionary key lookup to get the handler function
# keyError if cond can't be found in the dictionary
cond = 'cond_a'
func_dict[cond]()

# Python dicts have a get() method on them that returns the value for a given key, or a default value if the key can’t
# be found.
# if the condition can’t be found in the dictionary, we avoid raising a KeyError and call the default handler function
# instead.
func_dict.get(cond, handle_default)()

# use a dictionary to map opcodes to arithmetic operations with first-class functions
# Implicit return None statement as default if operator does not exist
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


# 7.4: Dict Expression
{True: 'yes', 1: 'no', 1.0: 'maybe'}
# {True: 'maybe'}
# Key: Python’s dictionaries don’t update the key object itself when a new value is associated with it.
# because the keys True, 1, and 1.0 all compare as equal, and they all have the same hash value.
# >>> True == 1 == 1.0
# True
# >>> (hash(True), hash(1), hash(1.0))
# (1, 1, 1)

# Value: As the interpreter evaluates the dictionary expression, it repeatedly overwrites the value for the key True.

# -Dictionaries treat keys as identical if their __eq__ comparison result says they’re equal and their hash values
# are the same.
# -Unexpected dictionary key collisions can and will lead to surprising results.


# 7.5 Merge Dictionaries
xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}
# classical solution: use the built-in dictionary update()
zs = {}
zs.update(xs)
zs.update(ys)
# zs: {'a': 1, 'b': 3, 'c': 4}

# Another technique: combined with the **-operator for "unpacking" objects
zs = dict(xs, **ys)
# zs: {'a': 1, 'b': 3, 'c': 4}

# Python 3.5+
zs = {**xs, **ys}
# zs: {'a': 1, 'b': 3, 'c': 4}

# Key Takeaways:
# In Python 3.5 and above you can use the **-operator to merge multiple dictionary objects into one
# with a single expression, overwriting existing keys left-to-right.
# To stay compatible with older versions of Python, you might want to use the built-in dictionary update() method
# instead.


# 7.6 Pretty-Printing
mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
# use json.dumps() to pretty-print Python dicts with nicer formatting
import json
json.dumps(mapping, indent=4, sort_keys=True)
# { "a": 23, "b": 42, "c": 12648430 } Printing dictionaries with the json module only works with dicts that can be
# serialized by it. As of Python 3.75, the supported built-in types are:
#   -dict
#   -list, tuple
#   -str
#   -int, float (and some Enums)
#   -bool
#   -None

# The classical solution to pretty-printing objects in Python is the built-in pprint module.
#
import pprint
pprint.pprint(mapping)
# {'a': 23, 'b': 42, 'c': 12648430, 'd': set([1, 2, 3])}
#
# Key Takeaways:
# The pprint and json module are “higher-fidelity” options built into the Python standard library.
# Be careful to only use json.dumps() on JSON-serializable keys and values, otherwise it raises a TypeError.

