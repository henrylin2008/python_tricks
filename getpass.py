# https://www.youtube.com/watch?v=C-gEQdGVXbk&t=561s

# username = input('Username: ')
# password = input('Password: ')  # clear text in display
#
# print()


from getpass import getpass

username = input('Username: ')
password = getpass('Password: ') # no text entered in the display 

print("Logging in... ")