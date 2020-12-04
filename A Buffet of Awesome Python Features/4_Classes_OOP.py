# 4.1 Object Comparisons: "is" vs "=="
# -An is expression evaluates to True if two variables point to the same (identical) object.
# -An == expression evaluates to True if the objects referred to by the variables are equal (have the same contents).
#
#
# 4.2 String Conversion (Every Class Needs a __repr__)
# By default all you get is a string containing the class name and the id of the object instance (which is the object’s
# memory address in CPython.)
# add a __str__ method to the Car class: printing the object (instead of id of the object instance)
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):  # convert an object into a string
        return '__str__ for Car'


my_car = Car('red', 37281)
print(my_car)
# __str__ for Car
'{}'.format(my_car)
# '__str__ for Car'
my_car
# __repr__ for Car

# To manually choose between both string conversion methods, for example, to express your code’s intent more clearly,
# it’s best to use the built-in str() and repr() functions.
str(my_car)
# '__str__ for Car'
repr(my_car)


# '__repr__ for Car'


# The benefit is you won’t have to modify the __repr__ implementation when the class name changes.
def __repr__(self):
    return (f'{self.__class__.__name__}('
            f'{self.color!r}, {self.mileage!r})')


repr(my_car)
# 'Car(red, 37281)'
print(my_car)
# 'Car(red, 37281)'
str(my_car)


# 'Car(red, 37281)'

# Key Takeaways
# -The result of __str__ should be readable. The result of __repr__ should be unambiguous.
# -Always add a __repr__ to your classes. The default implementation for __str__ just calls __repr__.
# -Use __unicode__ instead of __str__ in Python 2.

# 4.3 Defining Your Own Exception Classes
# Build meaningful custom exception (instead of built-in exception)
# Easy for troubleshooting
class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


# Exception Hierarchy
# declare a base class
class BaseValidationError(ValueError):
    pass

# "Real" Error Classes derived from the base error class
class NameTooShortError(BaseValidationError):
    pass

class NameTooLongError(BaseValidationError):
    pass

class NameTooCuteError(BaseValidationError):
    pass

# handle all of the errors
# try:
#     validate(name)
# except BaseValidationError as err:
#     handle_validation_error(err)

# defining custom exception classes makes it easier for your users to adopt an it’s easier to ask for forgiveness
# than permission (EAFP) coding style that’s considered more Pythonic.
#
# Key Takeaways:
# -Defining your own exception types will state your code’s intent more clearly and make it easier to debug.
# -Derive your custom exceptions from Python’s built-in Exception class or from more specific exception classes like
# ValueError or KeyError.
# -You can use inheritance to define logically grouped exception hierarchies.

# 4.4 Cloning Objects for Fun and Profit
# A shallow copy means constructing a new collection object and then populating it with references to the child objects
# found in the original. In essence, a shallow copy is only one level deep. The copying process does not recurse and
# therefore won’t create copies of the child objects themselves.
# A deep copy makes the copying process recursive. It means first constructing a new collection object and then
# recursively populating it with copies of the child objects found in the original.
#
# Shallow copy: copy.copy()
# Deep copy
import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
xs
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Both objects, the original and the copy, are fully independent this
# time. xs was cloned recursively, including all of its child objects:
xs[1][0] = 'X'
xs
# [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
zs
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

