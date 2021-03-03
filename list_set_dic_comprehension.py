# list comprehension:
import math

nums = [49, 64, 81, 100, 121]
# print result of square root with reminder of 0
new_list = [math.sqrt(n) for n in nums if n % 2 == 0]
print(new_list)     # [8.0, 10.0]


# Multiple loops in List comprehension
t1 = ["John", "Avi", "Mary"]
t2 = ["Evan", "Jack", "Jerry"]
new_list = [(x, y) for x in t1 for y in t2]
print(new_list)
# [('John', 'Evan'), ('John', 'Jack'), ('John', 'Jerry'), ('Avi', 'Evan'), ('Avi', 'Jack'), ('Avi', 'Jerry'),
# ('Mary', 'Evan'), ('Mary', 'Jack'), ('Mary', 'Jerry')]

