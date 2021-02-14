# Regular expressions are notorious for their seemingly strange syntax. This strange syntax is a byproduct of their
# flexibility. Regular expressions have to be able to filter out any string pattern you can imagine, which is why
# they have a complex string pattern format.
import re

text = "The person's phone number is 408-555-1234. Call soon!"
pattern = 'phone'
match = re.search(pattern, text)    # find first match, <re.Match object; span=(13, 18), match='phone'>
match.span()    # (13, 18)
match.start()   # 13
match.end()     # 18

text = "my phone is a new phone"
matches = re.findall("phone", text)     # find all matches
matches     # ['phone', 'phone']
len(matches)    # 2

for match in re.finditer('phone', text):
    print(match.span())     # (3, 8), (18, 23)
    print(match.group())    # phone, phone

# Patterns
# Character	Description	        Example Pattern    Example Match
# \d	    A digit	            file_\d\d          file_25
# \w	    Alphanumeric	    \w-\w\w\w	       A-b_1
# \s	    White space	        a\sb\sc	           a b c
# \D	    A non digit	        \D\D\D	           ABC
# \W	    Non-alphanumeric	\W\W\W\W\W	       *-+=)
# \S	    Non-whitespace	    \S\S\S\S	       Yoyo
text = "My telephone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
phone   # <re.Match object; span=(23, 35), match='408-555-1234'>
phone.group()   # '408-555-1234'

# Quantifiers
# Now that we know the special character designations, we can use them along with quantifiers to define
# how many we expect.
# Character	Description         Example Pattern Code	Example Match
# +	        1 or more times	    Version \w-\w+	        Version A-b1_1
# {3}	    exactly 3 times	    \D{3}	                abc
# {2,4}	    2 to 4 times	    \d{2,4}	                123
# {3,}	    3 or more	        \w{3,}	                anycharacters
# \*	    0 or more times	    A\*B\*C*	            AAACC
# ?	        Once or none        plurals?	            plural
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)   # same as above
# Groups
# What if we wanted to do two tasks, find phone numbers, but also be able to quickly extract their area code (
# the first three digits). We can use groups for any general task that involves grouping together regular expressions
# (so that we can later break them down).
#
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # group patterns
results = re.search(phone_pattern, text)
results.group()     # '408-555-1234'
results.group(1)    # '408'
results.group(2)    # '555'
results.group(3)    # '1234'
results.groups()    # ('408', '555', '1234')


# Additional Regex Syntax
# |: or, find 1st match of 'man' or 'woman'
re.search(r"man|woman", "This man was here.")   # re.Match object; span=(5, 8), match='man'>

# .: one; ..: two, ...: three
re.findall(r".at", "The cat in the hat sat here.")  # ['cat', 'hat', 'sat']

# One or more non-whitespace that ends with 'at'
re.findall(r'\S+at', "The bat went splat")  # ['bat', 'splat']

# Starts with and Ends With
# We can use the ^** to signal starts with, and the **$ to signal ends with:
# check first item in text is a number
re.findall(r'^\d', '1 is a number')    # ['1']

# last item in text is a digit/number
re.findall(r'\d$', '1 is a number 2')   # ['2']


# Exclusion
# To exclude characters, we can use the ^** symbol in conjunction with a set of brackets **[]. Anything inside the
# brackets is excluded. For example:
phrase = "there are 3 numbers 34 inside 5 this sentence."
pattern = r'[^\d]+' # excluding any digit/numbers
re.findall(pattern, phrase) # ['there are ', ' numbers ', ' inside ', ' this sentence.']

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
re.findall(r'[^!.?]+', test_phrase)     # excluding any punctuation of !.?
# ['This is a string', ' But it has punctuation', ' How can we remove it']
clean = re.findall(r'[^!.? ]+', test_phrase)   # excluding !.? (and space)
# ['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'How', 'can', 'we', 'remove', 'it']
' '.join(clean)
# 'This is a string But it has punctuation How can we remove it'

# Brackets for Grouping
text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
pattern = r'[\w]+-[\w]+'    # same as r'\w+-\w+' (without [])
re.findall(pattern, text)   # ['hypen-words', 'long-ish']

# Parenthesis for Multiple Options
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"
re.search(r'cat(fish|nap|erpillar)', text)
# <re.Match object; span=(27, 34), match='catfish'>
re.search(r'cat(fish|nap|erpillar)', texttwo)
# <re.Match object; span=(32, 38), match='catnap'>
re.search(r'cat(fish|nap|erpillar)', textthree)
# <re.Match object; span=(26, 37), match='caterpillar'>
