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
for idx, num in enumerate(data):    # better solution
    if num < 0:
        data[idx] = 0
end_time2 = time.time() - start_time2
print(end_time2)     # 4.29153e-06
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
squares2 = [i*i for i in range(100)]
# print(squares2)
end_time1 = time.time() - start_time1
print(end_time1)    # 1.09e-05


# 3.

