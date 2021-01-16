# Advanced Numbers
# Problem 1: Convert 1024 to binary and hexadecimal representation:
#
# In [6]:
print bin(1024)
print hex(1024)
# 0b10000000000
# 0x400

# Problem 2: Round 5.23222 to two decimal places

# In [5]:
round(5.23222,2)
# Out[5]:
# 5.23
#
# Advanced Strings
# Problem 3: Check if every letter in the string s is lower case
#
# In [7]:
s = 'hello how are you Mary, are you feeling okay?'

s.islower()
# Out[7]:
# False


# Problem 4: How many times does the letter 'w' show up in the string below?
#
# In [8]:
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
s.count('w')
# Out[8]:
# 12
#
#
# Advanced Sets
# Problem 5: Find the elements in set1 that are not in set2:
#
# In [12]:
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

set1.difference(set2)
# Out[12]:
# {2}



# Problem 6: Find all elements that are in either set:
#
# In [16]:
set1.union(set2)
# Out[16]:
# {1, 2, 3, 5, 6, 7, 8}


# Advanced Dictionaries
# Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using dictionary comprehension.
#
# In [17]:
{x:x**3 for x in range(5)}
# Out[17]:
# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

# Advanced Lists
# Problem 8: Reverse the list below:
#
# In [22]:
l = [1,2,3,4]

l.reverse()

l
# Out[22]:
# [4, 3, 2, 1]


# Problem 9: Sort the list below
#
# In [24]:
l = [3,4,2,5,1]

l.sort()

l
# Out[24]:
# [1, 2, 3, 4, 5]