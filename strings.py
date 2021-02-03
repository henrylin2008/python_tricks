# Escape Characters: 
# Escape char | Prints as
# 	\'		  | Single Quote
# 	\"		  | Doulbe Quote
# 	\t		  | Tab
# 	\n 		  | Newline (line break)	   
# 	\\		  | Backslash 

# methods:
spam = 'Hello world'
spam.upper()    # 'HELLO WORLD!'
spam.lower()    # 'hello world!'
spam.isupper()  # return boolean: False; all characters need to be upper case
spam.islower()    # return boolean: False, all characters need to be lower case

spam.isalpha()  # letters only; 'hello'
spam.isalnum()  # letters and number only; 'hello123'
spam.isdecimal()    # numbers only;  '123'
spam.isspace()  # whitespace only;  ' '
spam.istitle()  # title case only; 'This Is Title Case'

spam.startswith('Hello')    # return True
spam.startswith('H')    # True
spam.endswith('world!')  # Ture

','.join(['cats', 'rats', 'bats'])  # 'cats,rats,bats'
'Hello World'.split()   # ['Hello', "World']
'My name is Simon'.split('m')   # ['My na', 'e is Si', 'on']

'Hello'.rjust(10)   # '      Hello'; total length is 10
'Hello'.rjust(10, '*')  # '*****Hello';
'Hello'.ljust(10)   # 'Hello      '; total length is 10
'Hello'.ljust(10, '*')  # 'Hello*****'
'Hello'.center(10)  # '   Hello  '

'   Hello'.strip()  # 'Hello'
'     x     '.strip()    # 'x'
'     x     '.lstrip()   # 'x      '
'     x     '.rstrip()   # '      x'
'SpamSpamBaconSpamEggsSpamSpam'.strip('amps')   # 'BaconSpamEggs'

spam = 'Hello there!'
spam.replace('e', 'xyz')    # 'Hxyzllo thxyzrxyz!'


# pyperclip # need to be installed
import pyperclip
pyperclip.copy('Hello!!')
pyperclip.paste()   # 'Hello!!'