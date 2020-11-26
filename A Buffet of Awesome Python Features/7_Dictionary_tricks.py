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
# Implicit return None statement as default
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()
