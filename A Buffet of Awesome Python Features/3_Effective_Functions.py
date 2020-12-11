# 3 Effective Functions
# 3.1 Python's Functions are First-Class
# Python attaches a string identifier to every function at creation time for debugging purposes. You can access this
# internal identifier with the __name__ attribute:
#
def yell(text):
    return text.upper() + '!'

bark = yell

bark.__name__
# 'yell'

# Functions Can Be Stored in Data Structures
#
