name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}


# 7.1: Dictionary Default values
# Easier to ask for forgiveness than permission (EAFP), try & except to catch KeyError
def greeting(userid):
    try:
        return 'Hi %s!' % name_for_userid[userid]
    except KeyError:
        return 'Hi there'


# >>> greeting(382)
# 'Hi Alice!'
#
# >>> greeting(33333333)
# 'Hi there!'


# When get() is called, it checks if the given key exists in the dictionary. If it does, the value for the key is
# returned. If it does not exist, then the value of the default parameter is returned instead.
def greeting(userid):
    return 'Hi %s!' % name_for_userid.get(userid, 'there')


# 7.2: Sorting Dictionary
xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}

# To compare two tuples, Python compares the items stored at index zero. If they differ, this defines the outcome of
# the comparison. If they’re equal, the next two items at index one are compared, and so on.ßß
sorted(xs.items())
# [('a', 4), ('b', 3), ('c', 2), ('d', 1)]ß

# get a sorted representation of a dictionary based on its values (second element)
sorted(xs.items(), key=lambda x: x[1])
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
# sorted(xs.items(), key=lambda x: abs(x[1])), get absolute value of second item

# using operator; ex: operator.itemgetter, operator.attrgetter
import operator

sorted(xs.items(), key=operator.itemgetter(1))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]


# reverse the sort order so that larger values go first
sorted(xs.items(),
       key=lambda x: x[1],
       reverse=True)
# [('a', 4), ('b', 3), ('c', 2), ('d', 1)]


# 7.3 Emulating Switch/Case
