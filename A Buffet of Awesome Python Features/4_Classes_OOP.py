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

