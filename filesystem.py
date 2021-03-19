import os
from pathlib import Path


Path.home()    # current user's home directory
Path.cwd()     # path object represents current working directory
Path.cwd() / Path('Python_Pro') / Path('OOP') / Path('quiz_game')   # adding path to current working directory
# PosixPath('/Users/hlin/Documents/GitHub/python_tricks/Python_Pro/OOP/quiz_game')
os.chdir(Path.home())      # change to user's home directory
# Absolute paths (begin with the root folder / or c:\)
# Relative folders (do not begin with the root folder)
