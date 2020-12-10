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
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # make a shallow copy

xs.append(['new sublist'])
# >>> xs
# [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['new sublist']]
# >>> ys
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
xs[1][0] = 'X'
xs
# [[1, 2, 3], ['X', 5, 6], [7, 8, 9], ['new sublist']]
ys
# [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]

# Deep copy: copy.deepcopy()
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

# Copying Arbitrary Objects

# Key Takeaways
# -Making a shallow copy of an object won’t clone child objects. Therefore, the copy is not fully independent of the
#  original.
# -A deep copy of an object will recursively clone child objects. The clone is fully independent of the original, but
#  creating a deep copy is slower.
# -You can copy arbitrary objects (including custom classes) with the copy module.

# 4.5 Abstract Base Classes Keep Inheritance in Check
# Abstract Base Classes (ABCs) ensure that derived classes implement particular methods from the base class.
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        pass

    # We forget to declare bar() again...

# The raised exception tells us which method or methods we’re missing:
c = Concrete()
# TypeError:
# "Can't instantiate abstract class Concrete
# with abstract methods bar"

# Without abc, we’d only get a NotImplementedError if a missing method was actually called.
# Using ABCs states the programmer’s intent clearly and thus makes the code more communicative.

# Key Takeaways
# -Abstract Base Classes (ABCs) ensure that derived classes implement particular methods from the base class at
# instantiation time.
# -Using ABCs can help avoid bugs and make class hierarchies easier to maintain.
#

# 4.6 What Namedtuples Are Good For
# Namedtuples are immutable containers, just like regular tuples; "write once, read many" principle
# Each object stored in them can be accessed through a unique (human-readable) identifier.
# ex:
from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
# First argument ('Car') is referred to as the "typename" in the Python docs
# Above code, same as defined a Car class manually and given it a constructor accepting a "color" and a "mileage" value
# Later can be called by the name (instead of the index)
# Car = namedtuple('Car', [
#     'color',
#     'mileage',
# ])

# summary
# namedtuples are a memory-efficient shortcut to defining an immutable class in Python manually.

# Subclassing Namedtuples
# Since they are built on top of regular Python classes, you can even add methods to a namedtuple object.
# The easiest way to create hierarchies of namedtuples is to use the base tuple’s _fields property:
Car = namedtuple('Car', 'color mileage')
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
# This gives the desired result:
ElectricCar('red', 1234, 45.0)
# ElectricCar(color='red', mileage=1234, charge=45.0)

# _asdict() helper method. It returns the contents of a namedtuple as a dictionary:
my_car._asdict()
# OrderedDict([('color', 'red'), ('mileage', 3812.4)])
# This is great for avoiding typos in the field names when generating JSON-output, for example:
json.dumps(my_car._asdict())
# '{"color": "red", "mileage": 3812.4}'

# _replace() function: it creates a (shallow) copy of a tuple and allows you to selectively replace some of its fields
my_car._replace(color='blue')
# Car(color='blue', mileage=3812.4)

# Lastly, the _make() classmethod can be used to create new instances of a namedtuple from a sequence or iterable:
Car._make(['red', 999])
# Car(color='red', mileage=999)

# Key Takeaways
# -collection.namedtuple is a memory-efficient shortcut to manually define an immutable class in Python.
# -Namedtuples can help clean up your code by enforcing an easier-to-understand structure on your data.
# -Namedtuples provide a few useful helper methods that all start with a single underscore, but are part of the public
#  interface. It’s okay to use them.


# 4.7 Class vs Instance Variable Pitfalls
# -Class variables are declared inside the class definition (but outside of
# any instance methods). They’re not tied to any particular instance of a class. Instead, class variables store their
# contents on the class itself, and all objects created from a particular class share access to the same set of class
# variables. This means, for example, that modifying a class variable affects all object instances at the same time.
# -Instance variables are always tied to a particular object instance. Their contents are not stored on the class,
# but on each individual object created from the class. Therefore, the contents of an instance variable are
# completely independent from one object instance to the next. And so, modifying an instance variable only affects
# one object instance at a time.
class Dog:
    num_legs = 4  # <- Class variable

    def __init__(self, name):
        self.name = name  # <- Instance variable


jack = Dog('Jack')
jill = Dog('Jill')
jack.name, jill.name
# ('Jack', 'Jill')

jack.num_legs, jill.num_legs
# (4, 4)
Dog.num_legs
# 4

# If you try to access an instance variable through the class, it’ll fail with an AttributeError. Instance variables
# are specific to each object instance and are created when the __init__ constructor runs—they don’t even exist on the
# class itself.

Dog.name
# AttributeError:
# "type object 'Dog' has no attribute 'name'"

# Key Takeaways
# -Class variables are for data shared by all instances of a class. They belong to a class, not a specific instance and
# are shared among all instances of a class.
# -Instance variables are for data that is unique to each instance. They belong to individual object instances and are
# not shared among the other instances of a class. Each instance variable gets a unique backing store specific to the
# instance.
# -Because class variables can be “shadowed” by instance variables of the same name, it’s easy to (accidentally)
# override class variables in a way that introduces bugs and odd behavior.
#

# 4.8 Instance, Class, and Static
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

# -Instance Methods:
# takes one parameter, self, which points to an instance of MyClass when the method is called.
# Through the self parameter, instance methods can freely access attributes and other methods on the same object. This
# gives them a lot of power when it comes to modifying an object’s state.
#
obj = MyClass()
obj.method()
# ('instance method called', <MyClass instance at 0x11a2>)

# -Class methods:
# @classmethod, take a cls parameter that points to the class, and not the object instance- when the method is called
# It can't modify object instance state; Class methods can still modify  class state that applies across all instances
# of the class
obj.classmethod()
# ('class method called', <class MyClass at 0x11a2>
# Python only allows one __init__ method per class. Using class methods makes it possible to add as many alternative
# constructors as necessary.


# -Static Methods:
# @staticmethod, takes no parameter
# It cannot modify object state or class state. Static methods are restricted in what data they can access—they’re
# primarily a way to namespace your methods.
obj.staticmethod()
# 'static method called'
# the static methods can neither access the object instance state nor the class state.
# Flagging a method as a static method is not just a hint that a method won’t modify class or instance state. As you’ve
# seen, this restriction is also enforced by the Python runtime.
# Static methods also have benefits when it comes to writing test code. code. Since the circle_area() method is
# completely independent from the rest of the class, it’s much easier to test.
#
#
# Key Takeaways
# -Instance methods need a class instance and can access the instance through self.
# -Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class
#  itself via cls.
# -Static methods don’t have access to cls or self. They work like regular functions but belong to the class’ namespace.
# -Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can
#  have definite maintenance benefits.





