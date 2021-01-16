# In this lecture we will learn about the various methods for sets that you may not have seen yet. We'll go over the basic ones you already know and then dive a little deeper.
#
# In [2]:
s = set()
add
# add elements to a set. Remember a set won't take duplicate elements and only present them once (thats why its called a set!)
#
# In [3]:
s.add(1)
# In [4]:
s.add(2)
# In [5]:
s
# Out[5]:
# {1, 2}
#
# clear
# removes all elements from the set
#
# In [6]:
s.clear()
# In [7]:
# s
# Out[7]:
set()

# copy
# returns a copy of the set. Note it is a copy, so changes to the original don't effect the copy.
#
# In [10]:
s = {1,2,3}
sc = s.copy()
# In [11]:
# sc
# Out[11]:
# {1, 2, 3}
# In [12]:
s
# Out[12]:
# {1, 2, 3}
# In [13]:
s.add(4)
# In [14]:
s
# Out[14]:
# {1, 2, 3, 4}
# In [15]:
sc
# Out[15]:
# {1, 2, 3}


# difference
# difference returns the difference of two or more sets. The syntax is:

# set1.difference(set2)
# For example:

# In [17]:
s.difference(sc)
# Out[17]:
{4}

# difference_update
# difference_update syntax is:

set1.difference_update(set2)
# the method returns set1 after removing elements found in set2

# In [19]:
s1 = {1,2,3}
# In [20]:
s2 = {1,4,5}
# In [21]:
s1.difference_update(s2)
# In [22]:
s1
# Out[22]:
# {2, 3}

# discard
# Removes an element from a set if it is a member.If the element is not a member, do nothing.

# In [23]:
# s
# Out[23]:
# {1, 2, 3}
# In [25]:
s.discard(2)
# In [26]:
s
# Out[26]:
# {1, 3}

#
# intersection and intersection_update
# Returns the intersection of two or more sets as a new set.(i.e. elements that are common to all of the sets.)

# In [34]:
s1 = {1,2,3}
# In [35]:
s2 = {1,2,4}
# In [36]:
s1.intersection(s2)
# Out[36]:
# {1, 2}
# In [37]:
s1
# Out[37]:
# {1, 2, 3}
# intersection_update will update a set with the intersection of itself and another.

# In [38]:
s1.intersection_update(s2)
# In [39]:
s1
# Out[39]:
# {1, 2}


# isdisjoint
# This method will return True if two sets have a null intersection.

# In [49]:
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
# In [50]:
s1.isdisjoint(s2)
# Out[50]:
# False
# In [51]:
s1.isdisjoint(s3)
# Out[51]:
# True

#
# issubset
# This method reports whether another set contains this set.

# In [53]:
s1
# Out[53]:
# {1, 2}
# In [54]:
s2
# Out[54]:
# {1, 2, 4}
# In [55]:
s1.issubset(s2)
# Out[55]:
# True

# issuperset
# This method will report whether this set contains another set.

# In [56]:
s2.issuperset(s1)
# Out[56]:
# True


# symmetric_difference and symmetric_update
Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)

# In [58]:
s1
# Out[58]:
# {1, 2}
# In [59]:
s2
# Out[59]:
# {1, 2, 4}
# In [60]:
s1.symmetric_difference(s2)
# Out[60]:
# {4}


# union
# Returns the union of two sets (i.e. all elements that are in either set.)

# In [62]:
s1.union(s2)
# Out[62]:
# {1, 2, 4}


# update
# Update a set with the union of itself and others.

# In [63]:
s1.update(s2)
# In [64]:
s1
# Out[64]:
# {1, 2, 4}