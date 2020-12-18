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
sorted(tuples, key=lambda x: x[1]) # sorting a list of tuples by the second value in each tuple
# [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]

# Key Takeaways
# -Lambda functions are single-expression functions that are not necessarily bound to a name (anonymous).
# -Lambda functions can’t use regular Python statements and always include an implicit return statement.
# -Always ask yourself: Would using a regular (named) function or a list comprehension offer more clarity?
#

