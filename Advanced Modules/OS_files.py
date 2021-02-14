# Getting Directories
# Python has a built-in os module that allows us to use operating system dependent functionality.
#
# You can get the current directory:
import os
os.getcwd()    # current working directory
# '/Users/hlin/Documents/GitHub/python_tricks'

os.listdir()    # list items in current working directory
# ['.DS_Store', 'unit_test.py', 'property.py', 'sending_emails.py', 'os_environment_variables.py', '__pycache__',
# 'error_handling.py', 'zip.py', 'context_managers.py', 'logs.py', ..]

os.listdir('/Users/hlin/Documents/Docker')  # list items in exact directory
# ['.DS_Store', 'test', 'Dockerfile', 'Docker_commands', 'docker_comands.rtf', '.idea']

# Moving Files
# You can use the built-in shutil module to to move files to different locations. Keep in mind, there are permission
# restrictions, for example if you are logged in a User A, you won't be able to make changes to the top level Users
# folder without the proper permissions
import shutil
shutil.move('source_file', '/Users/hlin/Documents/Docker')  # move source_file to Docker dir


# Deleting Files
# NOTE: The os module provides 3 methods for deleting files:
#
# -os.unlink(path) which deletes a file at the path your provide
# -os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
# -shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path. All of
#  these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. Instead
#  we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of permanent
#  removal.
import send2trash
send2trash.send2trash('practice.txt')   # sending practice.txt file to the trash can


# Walking through a directory
# Often you will just need to "walk" through a directory, that is visit every file or
# folder and check to see if a file is in the directory, and then perhaps do something with that file. Usually
# recursively walking through every file and folder in a directory would be quite tricky to program, but luckily the
# os module has a direct method call for this called os.walk(). Let's explore how it works.
file_path = '/Python Bootcamp'
for folder, sub_folders, files in os.walk(file_path):

    print("Currently looking at folder: " + folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: " + sub_fold)

    print('\n')

    print("THE FILES ARE: ")
    for f in files:
        print("\t File: " + f)
    print('\n')

    # Now look at subfolders

# Currently looking at folder: /Users/hlin/Documents/GitHub/python_tricks/Python Bootcamp
# THE SUBFOLDERS ARE:
# 	 Subfolder: Advanced Modules
# THE FILES ARE:
# 	 File: List_Comprehensions.py
# 	 File: Functions.py

# Currently looking at folder: /Users/hlin/Documents/GitHub/python_tricks/Python Bootcamp/Advanced Modules
# THE SUBFOLDERS ARE:
# THE FILES ARE:
# 	 File: Collections_Module.py
# 	 File: OS_files.py