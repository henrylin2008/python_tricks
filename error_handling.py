# Catching Specific Exceptions in Python
# try:
#    # do something
#    pass
#
# except ValueError:
#    # handle ValueError exception
#    pass
#
# except (TypeError, ZeroDivisionError):
#    # handle multiple exceptions
#    # TypeError and ZeroDivisionError
#    pass
#
# except:
#    # handle all other exceptions
#    pass

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1 / num
    print("reciprocal ", reciprocal)

# If we pass an odd number:
# Enter a number: 1
# Not an even number!

# If we pass an even number, the reciprocal is computed and displayed.
# Enter a number: 4
# 0.25

# However, if we pass 0, we get ZeroDivisionError as the code block inside else is not handled by preceding except.
# Enter a number: 0
# Traceback (most recent call last):
#   File "<string>", line 7, in <module>
#     reciprocal = 1/num
# ZeroDivisionError: division by zero


# try...finally
# The try statement in Python can have an optional finally clause. This clause is executed no matter what, and is
# generally used to release external resources

try:
    f = open("test.txt", encoding='utf-8')  # perform file operations
finally:
    f.close()  # clean up the resource before the program comes to a halt whether it successfully ran or not


# Creating Custom Exceptions
# In Python, users can define custom exceptions by creating a new class. This exception
# class has to be derived, either directly or indirectly, from the built-in Exception class.

# When we are developing a large Python program, it is a good practice to place all the user-defined exceptions that
# our program raises in a separate file. Many standard modules do this. They define their exceptions separately as
# exceptions.py or errors.py (generally but not always).
#
# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")

# Enter a number: 12
# This value is too large, try again!
#
# Enter a number: 0
# This value is too small, try again!
#
# Enter a number: 8
# This value is too small, try again!
#
# Enter a number: 10
# Congratulations! You guessed it correctly.
