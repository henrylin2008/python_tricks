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
