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
# Functions can be nested
# Python allows functions to be defined inside other functions. These are often called nested functions or inner
# functions.

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'

    def yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


# get_speak_func doesn’t actually call any of its inner functions—it simply selects the appropriate inner function
# based on the volume argument and then returns the function object:


# Functions can capture local state
# Functions that do this are called lexical closures (or just closures, for short). A closure remembers the values from
# its enclosing lexical scope even when the program flow is no longer in that scope.
#


# Objects can behave like functions
# If an object is callable it means you can use the round parentheses function call syntax on it and even pass in
# function call arguments. This is all powered by the __call__ dunder method.
#
# there’s a built-in callable function to check whether an object appears to be callable or not:
callable(plus_3)
# True
callable(yell)
# True
callable('hello')
# False

# Key Takeaways
# -Everything in Python is an object, including functions. You can assign them to variables,
#  store them in data structures, and pass or return them to and from other functions (first-class functions.)
# -First-class functions allow you to abstract away and pass around behavior in your programs.
# -Functions can be nested and they can capture and carry some of the parent function’s state with them. Functions that
#  do this are called closures.
# -Objects can be made callable. In many cases this allows you to treat them like functions.
#

# 3.2 Lambdas are single-expression functions
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
sorted(tuples, key=lambda x: x[1])  # sorting a list of tuples by the second value in each tuple


# [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]

# Key Takeaways
# -Lambda functions are single-expression functions that are not necessarily bound to a name (anonymous).
# -Lambda functions can’t use regular Python statements and always include an implicit return statement.
# -Always ask yourself: Would using a regular (named) function or a list comprehension offer more clarity?
#

# 3.3 The Power of Decorators
# Decorators allow you to define reusable building blocks that can change or extend the behavior of other functions.
# And, they let you do that without permanently modifying the wrapped function itself. The function’s behavior changes
# only when it’s decorated.
# A decorator is a callable that takes a callable as input and returns another callable.
def null_decorator(func):
    return func


@null_decorator
def greet():
    return 'Hello!'


# Putting an @null_decorator line in front of the function definition is the same as defining the function first and
# then running through the decorator.


greet()


# 'Hello!'

# Key Takeaways:
# -Decorators define reusable building blocks you can apply to a callable to modify its behavior
#  without permanently modifying the callable itself.
# -The @ syntax is just a shorthand for calling the decorator on an input function. Multiple decorators on a single
#  function are applied bottom to top (decorator stacking).
# -As a debugging best practice, use the functools.wraps helper in your own decorators to carry over metadata from the
#  undecorated callable to the decorated one.
# -Just like any other tool in the software development toolbox, decorators are not a cure-all and they should not be
#  overused. It’s important to balance the need to “get stuff done” with the goal of “not getting tangled up in a
#  horrible, unmaintainable mess of a code base.”
#

# 3.4 Fun with *args & **kwargs
# What are *args and **kwargs parameters used for? They allow a function to accept
# optional arguments, so you can create flexible APIs in your modules and classes
def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


# *args will collect extra positional arguments as a tuple because the parameter name has a * prefix.
# **kwargs will collect extra keyword arguments as a dictionary because the parameter name has a ** prefix.
#
# Key Takeaways
# -*args and **kwargs let you write functions with a variable number of arguments in Python.
# -*args collects extra positional arguments as a tuple. **kwargs collects the extra keyword arguments as a dictionary.
# -The actual syntax is * and **. Calling them args and kwargs is just a convention (and one you should stick to).
#

# 3.5 Function Argument Unpacking
def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


genexpr = (x * x for x in range(3))
print_vector(*genexpr)
# Putting a * before an iterable in a function call will unpack it and pass its elements as separate positional
# arguments to the called function.

# Key Takeaways
# -The * and ** operators can be used to “unpack” function arguments from sequences and dictionaries.
# -Using argument unpacking effectively can help you write more flexible interfaces for your modules and functions.
#

# 3.6 Nothing to Return Here
# If a function doesn’t specify a return value, it returns None by default. This means you
# can replace return None statements with bare return statements or even leave them out completely and still get the
# same result
#
# Key Takeaways
# -If a function doesn’t specify a return value, it returns None. Whether to explicitly return None is a stylistic
# decision.
# -This is a core Python feature but your code might communicate its intent more clearly with an explicit return None
# statement.



