# 6.1 Writing Pythonic Loops
# The range type represents an immutable sequence of numbers. Its advantage over a regular list is that it always takes
# the same small amount of memory. Range objects don’t actually store the individual values representing the number
# sequence
my_items = ['a', 'b', 'c']

for i, item in enumerate(my_items):
    print(f'{i}: {item}')

# 0: a
# 1: b
# 2: c

emails = {
    'Bob': 'bob@example.com',
    'Alice': 'alice@example.com',
}

for name, email in emails.items():
    print(f'{name} -> {email}')

# 'Bob -> bob@example.com'
# 'Alice -> alice@example.com'

for i in range(a, n, s):    # a: start, n: stop, s: step
    # ...

# Key Takeaways:
# -Writing C-style loops in Python is considered unpythonic. Avoid managing loop indexes and stop conditions manually
#  if possible.
# -Python’s for-loops are really “for-each” loops that can iterate directly over items from a container or sequence.
#
#

# 6.2 Comprehending Comprehensions
# List Comprehensions is that they’re just for-loops over a collection but expressed in a more terse and compact syntax.
# values = [expression
#           for item in collection
#           if condition]
#
# Set Comprehension
{x * x for x in range(-9, 10)}
# set([64, 1, 36, 0, 49, 9, 16, 81, 25, 4])
# sets are an unordered collection type, "random" order"

# Dictionary Comprehension
{ x: x * x for x in range(5) }
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Key Takeaways:
# -Comprehensions are a key feature in Python. Understanding and applying them will make your code much more Pythonic.
# -Comprehensions are just fancy syntactic sugar for a simple for-loop pattern. Once you understand the pattern, you’ll
#  develop an intuitive understanding for comprehensions.
# -There are more than just list comprehensions.
#

# 6.3 List Slicing Tricks and the Sushi Operator
# Syntax: [start:stop:step]
# step defaults to one (if it's not included)
# stride: (ex: sublist every other element of the list:
lst = [1,2,3,4,5]
lst[::2]
# [1,3,5]
lst[::-1]   # same as list.reverse() or reversed() to reverse a list
# [5,4,3,2,1]

# You can use the :-operator to clear all elements from a list without destroying the list object itself.

del lst[:]  # same as lst.clear() (available in Python 3)
lst
# []

# Key Takeaways
# -The : “sushi operator” is not only useful for selecting sublists of elements within a list. It can also be used to
#  clear, reverse, and copy lists.
# -But be careful—this functionality borders on the arcane for many Python developers. Using it might make your code
#  less maintainable for everyone else on your team.
#

# 6.4 Beautiful Iterators

# Iterators use exceptions to structure control flow. To signal the end of iteration, a Python iterator simply raises
# the built-in StopIteration exception.

# Key Takeaways
# -Iterators provide a sequence interface to Python objects that’s memory efficient and considered Pythonic. Behold the
#  beauty of the for-in loop!
# -To support iteration an object needs to implement the iterator protocol by providing the __iter__ and __next__ dunder
#  methods.
# -Class-based iterators are only one way to write iterable objects in Python. Also consider generators and generator
#  expressions.

# 6.5 Generators Are Simplified Iterators
def repeater(value):
    while True:
        yield value
# Yield returns a generator object to the caller, and the execution of the code starts only when the generator is
# iterated.
# Whereas a return statement disposes of a function’s local state, a yield statement suspends the function and retains
# its local state.
#
# Key Takeaways
# -Generator functions are syntactic sugar for writing objects that support the iterator protocol. Generators abstract
#  away much of the boilerplate code needed when writing class-based iterators.
# -The yield statement allows you to temporarily suspend execution of a generator function and to pass back values from
#  it.
# -Generators start raising StopIteration exceptions after control flow leaves the generator function by any means other
#  than a yield statement.
#


