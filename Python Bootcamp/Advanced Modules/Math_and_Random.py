# Math and Random Modules
# Python comes with a built in math module and random module. In this lecture we will give a
# brief tour of their capabilities. Usually you can simply look up the function call you are looking for in the
# online documentation.
#
# Math Module

import math

value = 4.35
math.floor(value)  # 4
math.ceil(value)  # 5
round(4.5)  # 4
round(5.5)  # 6 (half num down and half num up to balance the round function)
math.pi  # 3.141592653589793

from math import pi

pi  # 3.141592653589793

math.e  # 2.718281828459045
math.inf  # inf
math.nan  # nan
math.log(100, 10)  # 2: 10 ^ 2 == 100

# Random Module
# Random Module allows us to create random numbers. We can even set a seed to produce the same random set every time.
#
# The explanation of how a computer attempts to generate random numbers is beyond the scope of this course since it
# involves higher level mathmatics. But if you are interested in this topic check out:
#
# https://en.wikipedia.org/wiki/Pseudorandom_number_generator
# https://en.wikipedia.org/wiki/Random_seed

# Understanding a seed
# Setting a seed allows us to start from a seeded pseudo random number generator, which means the same random numbers
# will show up in a series. Note, you need the seed to be in the same cell if your using jupyter to guarantee the
# same results each time. Getting a same set of random numbers can be important in situations where you will be
# trying different variations of functions and want to compare their performance on random values, but want to do it
# fairly (so you need the same set of random numbers each time).
import random

random.randint(0, 100)  # random int number between 0 and 100

random.seed(101)  # any number would do, same random numbers will show up in a series
random.randint(0, 100)  # 74
random.randint(0, 100)  # 24
random.randint(0, 100)  # 69

mylist = list(range(0, 20))
mylist  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
random.choice(mylist)   # 17
# Sample with replacement, can have duplicate numbers
random.choices(population=mylist, k=10)  # [18, 9, 13, 4, 4, 5, 13, 4, 19, 1]
# Sample without replacement, no duplicate numbers
random.sample(population=mylist, k=10)   # [6, 5, 2, 14, 11, 3, 7, 12, 18, 16]

random.shuffle(mylist)  # permanently change the order of the list
mylist  # [16, 14, 0, 8, 11, 17, 19, 15, 5, 9, 10, 1, 3, 4, 7, 18, 2, 6, 13, 12]

# Continuous, random picks a value between a and b, each value has equal change of being picked.
random.uniform(a=0, b=100)  # 74.44690143237648
