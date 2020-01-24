# https://www.youtube.com/watch?v=C-gEQdGVXbk&t=561s
# class Person():
#     pass
#
# person = Person()
#
# first_key = 'first'
# first_val = 'Corey'
#
# setattr(person, first_key, first_val) # (object, name, value)
#
# first = getattr(person, first_key)
#
# print(first) #Corey
# # print(person.first) # output: Corey (with only seattr)



########################################################################

class Person():
    pass

person = Person()
person_info = {'first': 'Corey', 'last': "Schafer"}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))