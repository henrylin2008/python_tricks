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
