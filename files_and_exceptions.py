# open pi_digits.txt in read mode (default) on current directory
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())  # remove any spaces on the right of the contents

# relative path: current directory or current_folder/subdir_file
# absolute path: exact location: ex: '/home/hlin/files/text_files/filename.txt'

# readlines(): takes each line from the file and stores it in a list

# write to a file
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.")

# w (write): erase the contents of the file before returning the file object
# a (append): add content to the end of the file
# r+ (read and write mode)

# Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to
# convert the data to string format first using the str() function.

# Exception
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# Storing data:
# The json.dump() function takes two arguments: a piece of data to store and a file object it can use to store the data.
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)   # store the list numbers in the file numbers.json


import json
filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)  # load the information stored in numbers.json, and assign it to the variable numbers
print(numbers)

