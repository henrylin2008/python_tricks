# 1. Iterate with enumerate() instead of range(len())
import time

data = [1, 2, -4, -3, 5, 3, -2, -8, -9, 10, 8, 9, 4, -5, -8, -4]
#
# start_time = time.time()
# for i in range(len(data)):
#     if data[i] < 0:
#         data[i] = 0
# print(data)
# end_time = time.time() - start_time
# print(end_time)     # 2.31266e-5
#
# enumerate:
start_time2 = time.time()
for idx, num in enumerate(data):  # better solution
    if num < 0:
        data[idx] = 0
end_time2 = time.time() - start_time2
print(end_time2)  # 4.29153e-06
#

# 2. Use List Comprehensions instead of for raw loops

# squares = []
# start_time = time.time()
# for i in range(100):
#     squares.append(i*i)
# # print(squares)
# end_time = time.time() - start_time
# print(end_time)     # 3.099e-05

# List Comprehension, better and faster
start_time1 = time.time()
squares2 = [i * i for i in range(100)]
# print(squares2)
end_time1 = time.time() - start_time1
print(end_time1)  # 1.09e-05

# 3. Sort complex iterables with sorted()

data = (3, 5, 1, 10, 9)
sorted_data = sorted(data, reverse=True)
print(sorted_data)  # [10, 9, 5, 3, 1]

data1 = [{"name": "Max", "age": 6},
         {"name": "Lisa", "age": 20},
         {"name": "Ben", "age": 9}]

sorted_data2 = sorted(data1, key=lambda x: x["age"])  # sorted with keyword
print(sorted_data2)
# [{'name': 'Max', 'age': 6}, {'name': 'Ben', 'age': 9}, {'name': 'Lisa', 'age': 20}]


# 4.Save Memory with Generators: one item at a time
import sys

my_list = [i for i in range(10000)]
print(sum(my_list))  # 49995000
print(sys.getsizeof(my_list), "bytes")  # 87624 bytes

my_gen = (i for i in range(10000))
print(sum(my_gen))  # 49995000
print(sys.getsizeof(my_gen), "bytes")  # 120 bytes (one item at a time)


# 5. Default values in dictionaries with .get() and .setdefault()

my_dict = {"item": "football", "price": 10.00}
count = my_dict.get("count", 0)     # print default value 0; if 0 is not set, default value is None
print(count)        # 0

count = my_dict.setdefault("count", 0)      # add "count" with value 0 into my_dict
print(count)    # 0
print(my_dict)      # {'item': 'football', 'price': 10.0, 'count': 0}


# 6. Count hashable objects with collections.Counter
from collections import Counter

my_list = [10, 10, 10, 5, 5, 5, 3, 2, 3, 4, 4, 5, 3, 2, 3, 4]
counter = Counter(my_list)
print(counter)   # Counter({5: 4, 3: 4, 10: 3, 4: 3, 2: 2}); sorted with most items in the front
print(counter[5])     # 4
print(counter[15])    # 0 for non-exist item in counter list

most_common = counter.most_common(2)    # most 2 common items
print(most_common)          # returns tuple: [(5, 4), (3, 4)]; (item, count)
print(most_common[0][0])    # 5; most common item value


# 7.Concatenate string with .join()
list_strings = ["Hello", "my", "friend"]
" ".join(list_strings)      # "Hello my friend"


# 8. Merge dictionaries with {**d1, **d2} (3.5+)
d1 = {"name": "Alex", "age": 25}
d2 = {"name": "Alex", "city": "SF"}
merged_dict = {**d1, **d2}
print(merged_dict)      # {'name': 'Alex', 'age': 25, 'city': 'SF'}

