#unpacking
a, _ = (1, 2) # _ = variable not going to use
print(a) # 1
# print(b)


b, c, *d = (1,2,3,4,5)  # *d = everything after (1, 2)
print(b) # 1
print(c) # 2
print(d) # [3,4,5]


b, c, *_ = (1,2,3,4,5)  # *d = everything after (1, 2)
print(b) # 1
print(c) # 2
# print(d) # [3,4,5]


b, c, *d, e = (1,2,3,4,5)
print(b) # 1
print(c) # 2
print(d) # [3, 4]
print(e) # 5


b, c, *_, e = (1,2,3,4,5) # *_: ignore numbers in between
print(b) # 1
print(c) # 2
print(e) # 5
