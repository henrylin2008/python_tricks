# open pi_digits.txt in read mode (default) on current directory
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())   # remove any spaces on the right of the contents

# relative path: current directory or current_folder/subdir_file
# absolute path: exact location: ex: '/home/hlin/files/text_files/filename.txt'

