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
