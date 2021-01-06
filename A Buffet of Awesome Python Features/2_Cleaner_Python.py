# 2 Patterns for Cleaner Python
# 2.1 Covering Your A** with Assertions
# Python’s assert statement is a debugging aid that tests a condition. If the assert condition is true, nothing happens,
# and your program continues to execute as normal. But if the condition evaluates to false, an AssertionError exception
# is raised with an optional error message.
#
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

# Assert will guarantee that, no matter what, discounted prices calculated by this function cannot be lower than $0 and
# they cannot be higher than product’s original price.
# 14900 instead of $149.00
shoes = {'name': 'Fancy Shoes', 'price': 14900}

apply_discount(shoes, 2.0)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#     apply_discount(prod, 2.0)
#   File "<input>", line 4, in apply_discount
#     assert 0 <= price <= product['price']
# AssertionError
# the exception stacktrace points out the exact line of code containing the failed assertion.
#

# the proper use of assertions is to inform developers about unrecoverable errors in a program. Assertions are not
# intended to signal expected error conditions, like a File-Not-Found error, where a user can take corrective actions
# or just try again. Assertions are meant to be internal self-checks for your program.
# The goal of using assertions is to let developers find the likely root cause of a bug more quickly.
#
# Assert statement
assert_stmt ::= "assert" expression1 ["," expression2]
# expression1 is the condition we test, and the optional expression2 is an error message that’s displayed if the
# assertion fails.

# Caveats
# Caveat #1 - Don't use asserts for data validation
# The biggest caveat with using asserts in Python is that assertions can be globally disabled3 with the -O and -OO
# command line switches, as well as the PYTHONOPTIMIZE environment variable in CPython.
# Never use assertions to do data validation
#
# Caveat #2 – Asserts That Never Fail
# If you pass a tuple to an assert statement, it leads to the assert condition always being true—which in turn leads to
# the above assert statement being useless because it can never fail and trigger an exception.
#
# Key Takeaways
# -Python’s assert statement is a debugging aid that tests a condition as an internal self-check in your program.
# -Asserts should only be used to help developers identify bugs. They’re not a mechanism for handling run-time errors.
# -Asserts can be globally disabled with an interpreter setting.
#
# 2.2 Complacent Comma Placement
# you can place a comma after every item in a list, dict, or set constant, including the last item.
#
names = [
    'Alice',
    'Bob',
    'Dilbert',
]
# Key Takeaways
# -Smart formatting and comma placement can make your list, dict, or set constants easier to maintain.
# -Python’s string literal concatenation feature can work to your benefit, or introduce hard-to-catch bugs.
#

# 2.3 Context Managers and the with Statement
# Opening files using the with statement is generally recommended because it ensures that open file descriptors are
# closed automatically after program execution leaves the context of the with statement.
#
with open('hello.txt', 'w') as f:
    f.write('hello, world!')
# Key Takeaways
# -The with statement simplifies exception handling by encapsulating standard uses of try/finally statements in
#  so-called context managers.
# -Most commonly it is used to manage the safe acquisition and release of system resources. Resources are acquired by
#  the with statement and released automatically when execution leaves the with context.
# -Using with effectively can help you avoid resource leaks and make your code easier to read.
#

# 2.4 Underscores, Dunders, and More
# 1. Single Leading Underscore:"_var"
# The underscore prefix is meant as a hint to tell another programmer that a variable or method starting with a single
# underscore is intended for internal use.
# if you use a wildcard import to import all the names from the module, Python will not import names with a leading
# underscore
# my_module.py:
def external_func():
    return 23

def _internal_func():
    return 42

from my_module import *
external_func()
# 23
_internal_func()
# NameError: "name '_internal_func' is not defined"

# 2. Single Trailing Underscore: "var_"
# In summary, a single trailing underscore (postfix) is used by convention to avoid naming conflicts with Python
# keywords.
#

# 3. Double Leading Underscore: "__var"
# A double underscore prefix causes the Python interpreter to rewrite the attribute name in order to avoid naming
# conflicts in subclasses.
#

# 4. Double leading and trailing underscore: "__var__"
# names that have both leading and trailing double underscores are reserved for special use in the language. This rule
# covers things like __init__ for object constructors, or __call__ to make objects callable.
# These dunder methods are often referred to as magic methods—
#

# 5. Single Underscore: "_"
# Per convention, a single stand-alone underscore is sometimes used as a name to indicate that a variable is temporary
# or insignificant.
# This is handy if you’re working in an interpreter session and you’d like to access the result of a previous calculation:
20 + 3
# 23
_
# 23
print(_)
# 23

# Key Takeaways
#-Single Leading Underscore “_var”: Naming convention indicating a name is meant for internal use. A hint for
#  programmers and not enforced by the interpreter (except in wildcard imports.)
#-Single Trailing Underscore “var_”: Used by convention to avoid naming conflicts with Python keywords.
#-Double Leading Underscore “__var”: Triggers name mangling when used in a class context. Enforced by the Python
#  interpreter.
#-Double Leading and Trailing Underscore “__var__”: Indicates special methods defined by the Python language. Avoid
#  this naming scheme for your own attributes.
#-Single Underscore “_”: Sometimes used as a name for temporary or insignificant variables (“don’t care”). Also, it
#  represents the result of the last expression in a Python REPL session.

# 2.5 A Shocking Truth about String Formatting
errno = 50159747054
name = 'Bob'
# 1-"Old Style" String Formatting
# Strings in Python have a unique built-in operation that can be accessed with the %-operator.
'Hello, %s' %name
# 'Hello, Bob'
'%x' % errno    # convert numbers to hexadecimal
# 'badc0ffee'
'Hey %s, there is a 0x%x error!' % (name, errno)
# 'Hey Bob, there is a 0xbadc0ffee error!'
'Hey %(name)s, there is a 0x%(errno)x error!' % { "name": name, "errno": errno }
# 'Hey Bob, there is a 0xbadc0ffee error!'

# 2-"New Style" String Formatting
# In Python 3, You can use the format() function to do simple positional formatting,
'Hello, {}'.format(name)
# 'Hello, Bob'

'Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno)
# 'Hey Bob, there is a 0xbadc0ffee error!'

# 3-Literal String Interpolation (Python 3.6+)
# Python 3.6 adds yet another way to format strings, called Formatted String Literals. This new way of formatting
# strings lets you use embedded Python expressions inside string constants.
f'Hello, {name}!'
# 'Hello, Bob!'
# you can embed arbitrary Python expressions, you can even do inline arithmetic with it,
a = 5
b = 10
f'Five plus ten is {a + b} and not {2 * (a + b)}.'
# 'Five plus ten is 15 and not 30.'

# 4-Template Strings
from string import Template
t = Template('Hey, $name!')
t.substitute(name=name)
# 'Hey, Bob!'
templ_string = 'Hey $name, there is a $error error!'
Template(templ_string).substitute(name=name, error=hex(errno))  #transform int error number into a hex-string
# 'Hey Bob, there is a 0xbadc0ffee error!'

# Rule of Thumb:
# If your format strings are user-supplied, use Template Strings to avoid security issues. Otherwise, use Literal String
# Interpolation if you’re on Python 3.6+, and “New Style” String Formatting if you’re not.

# Key Takeaways
# -Perhaps surprisingly, there’s more than one way to handle string formatting in Python.
# -Each Method has its individual pros and cons. Your use case will influence which method you should use.





