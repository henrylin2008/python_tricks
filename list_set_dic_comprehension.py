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


# Set comprehension:
word = "sweet"
new_word = {i for i in word}  # no repeat string
print(new_word)               # {'t', 's', 'e', 'w'}


# Dictionary Comprehension
nums = [1, 2, 3, 4, 5]
square_dict = {num: num**2 for num in nums}
print(square_dict)            # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Increase the price by 50% for any price > 2.0
old_price = {"milk": 1.02, "coffee": 2.5, "bread": 2.5}
new_price = {item: price*1.5 if price > 2 else price for (item, price) in old_price.items()}
new_price           # {'milk': 1.02, 'coffee': 3.75, 'bread': 3.75}
