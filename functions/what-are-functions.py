# Functions are interactions of objects.
## A function can take some objects and always gives something in return
## (even with no return statement, it's the None object).

# What function takes as its parameters is called a signature.
def func(a, /, b, *, c):
    #    ^^^^^^^^^^^^^
    # What is that?
    # - parameters
    # - arguments
    pass

import inspect  # noqa
print(inspect.signature(func))  # The signature is (a, /, b, *, c).

# Every function can take parameters and always returns something:
def func():
    return 1  # The return value of func() is always 1.

print(func())  # 1

def func():
    pass

#   ^^^^ 
# No return statement; the return value is always None.

# Summary
# Functions describe interactions between objects.
# Every function consists of a name (except for lambdas), signature (parameters), and the underlying code.
# The underlying code determines what the function does with the objects passed through parameters
# as well as provides the return value.
