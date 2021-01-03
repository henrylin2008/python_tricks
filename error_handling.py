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
