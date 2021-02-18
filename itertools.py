import itertools

# itertools.permutations() generates permutations for an iterable. Time to brute-force those passwords
for p in itertools.permutations('ABCD'):
    print(p)

# ('A', 'B', 'C', 'D')
# ('A', 'B', 'D', 'C')
# ('A', 'C', 'B', 'D')
# ('A', 'C', 'D', 'B')
# ('A', 'D', 'B', 'C')
# ('A', 'D', 'C', 'B')
# ('B', 'A', 'C', 'D')
# ('B', 'A', 'D', 'C')
# ('B', 'C', 'A', 'D')
# ('B', 'C', 'D', 'A')
# ('B', 'D', 'A', 'C')
# ('B', 'D', 'C', 'A')
# ('C', 'A', 'B', 'D')
# ('C', 'A', 'D', 'B')
# ('C', 'B', 'A', 'D')
# ('C', 'B', 'D', 'A')
# ('C', 'D', 'A', 'B')
# ('C', 'D', 'B', 'A')
# ('D', 'A', 'B', 'C')
# ('D', 'A', 'C', 'B')
# ('D', 'B', 'A', 'C')
# ('D', 'B', 'C', 'A')
# ('D', 'C', 'A', 'B')
# ('D', 'C', 'B', 'A')

# Product
from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))  # [(1, 3), (1, 4), (2, 3), (2, 4)]

a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))  # [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

# Permutations
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

perm = permutations(a, 2)   # 2 = length of arguments
print(list(perm))       # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


# Combinations
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)   # 2 = length
print(list(comb))       # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]; no reputation
comb_wr = combinations_with_replacement(a, 2)
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)], with reputation


# Accumulate
from itertools import accumulate
import operator
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)            # [1, 2, 3, 4]
print(list(acc))    # [1, 3, 6, 10]; accumulate sum
acc_product = accumulate(a, func=operator.mul)
print(list(acc_product))    # [1, 2, 6, 24]; accumulate product of last 2 numbers


# groupby
from itertools import groupby
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27},
           {'name': 'Claire', 'age': 28}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))
# 25[{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
# 27[{'name': 'Lisa', 'age': 27}]
# 28[{'name': 'Claire', 'age': 28}]


# Infinite Iterators: count, cycle, repeat
from itertools import count, cycle, repeat

for i in count(10): # starts at 10, until hits a break point
    print(i)
    if i == 15:
        break
# 10
# 11
# 12
# 13
# 14
# 15

a = [1, 2, 3]
for i in cycle(a):  # infinite loop, until interrupt by keyboard
    print(i)

for i in repeat(1, 4):  # repeat 1, 4 = number of times
    print(i)
