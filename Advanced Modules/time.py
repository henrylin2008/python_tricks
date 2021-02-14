# Timing your code
def func_one(n):
    """
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    """
    return [str(num) for num in range(n)]


def func_two(n):
    """
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    """
    return list(map(str, range(n)))


import time

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_one(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time  # 0.18550348281860352

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_two(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time  # 0.1496279239654541

### Timeit Module
# The timeit module takes in two strings, a statement (stmt) and a setup. It then runs the setup code and runs the
# stmt code some n number of times and reports back average length of time it took.
import timeit

setup = '''
def func_one(n  ):
    return [str(num) for num in range(n)]
'''
stmt = 'func_one(100)'
timeit.timeit(stmt, setup, number=100000)  # 1.3161248000000114

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
stmt2 = 'func_two(100)'
timeit.timeit(stmt2, setup2, number=100000)  # 1.0892171000000417

timeit.timeit(stmt, setup, number=1000000)   # 13.129837899999984
timeit.timeit(stmt2, setup2, number=1000000)    # 10.894090699999992

