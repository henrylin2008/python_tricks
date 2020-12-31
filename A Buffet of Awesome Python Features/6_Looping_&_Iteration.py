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

