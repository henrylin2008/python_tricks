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