# https://www.youtube.com/watch?v=C-gEQdGVXbk&t=561s
names = ['Corey', 'Chris', 'Dave', 'Travis']

# index = 0    #Beginner's code
# for name in names:
#     print(index, name)
#     index += 1

for index, name in enumerate(names, start=1): # index starts at 1
    print(index, name)