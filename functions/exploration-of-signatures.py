# "Signature" means: parameters of a function.

def foo(a, b):
    pass

# The signature of foo is (a, b).

def bar(_, /, a, *, b, **kwargs):
    pass

# The signature of bar is (_, /, a, *, b, **kwargs).

# Every signature can consist of several kinds of parameters.
# 1. Most popular: both positional and keyword argument.

def func(a):
    #   ^^^
    # Signature of func is (a).
    # The signatures consists of the following parameters:
    # - `a`, passed to func via:
    #      - func(1)    <-- `a` passed as a positional argument
    #      - func(a=1)  <-- `a` passed as a keyword argument
    print(a)

# By passing objects to a function positionally, we bind them to corresponding respective names.
# 1 -> a
func(1)
# `a` is defined as 1 inside func(), but not defined outside func():
try:
    print(a)  # type: ignore
except NameError:
    pass
# Defining `a` outside of func() does not change the value of `a` inside func():
a = 10
# A name of a variable can collide with a name of a parameter,
# but there is no implicit connection between them:
func(5)  # outside func() a = 10, inside func() a = 5.

a = 2  # `a` is set globally
func(3)  # `a` is set locally inside func() and doesn't influence the global `a`
#    ^
#    `a` passed as a positional argument
func(a=3)  # Same here. Global a is unchanged.
#    ^^^
#    `a` passed as a keyword argument

def check(a, b):
    # What is `a` here from the call in line 54? - 20 (global `b`)
    # What is `b` here from the call in line 54? - 10 (global `a`)
    pass

a = 10
b = 20
check(b, a)

# 2. Positional-only arguments
# Some parameters can only be passed positionally.

def posfunc(a, /):
    pass

posfunc(1)  # This is fine.

b = 1
posfunc(b)  # This is also fine.

try:
    posfunc(a=1)  # This is ILLEGAL! `a` is a POSITIONAL argument.
except TypeError:
    pass


def otherfunc(a, /, b):
    # `a` is a positional parameter. It can be passed in the following way(s):
    # - `otherfunc(1, ...)`
    # This is ILLEGAL:
    # - `otherfunc(a=1, ...)`
    # `b` is a positional AND keyword parameter at the same time. It can be passed in the following way(s):
    # - `otherfunc(..., 1)` (`b` passed positionally)
    # - `otherfunc(..., b=1)` (`b` passed through a keyword)
    pass


# Exercise:
# All LEGAL ways to call `otherfunc()`:
otherfunc(1, 1)
otherfunc(1, b=1)
# A few ILLEGAL ways to call `otherfunc()`
try: 
    # Place solutions here
    # `otherfunc(a=1, 1)`  is a syntax error.
    otherfunc(a=1, b=1)  # `a` is positional only.
except TypeError:
    pass

# Keyword-only arguments
# Some parameters can only be passed through keywords.

# Exercise: Google how to denote a keyword-only argument in a signature.
def kwfunc(*, a):
    #      ^
    #      Since the *, all the following parameters are keyword-only.
    pass

def mixedfunc(a, *, b):
    #         1  2  3
    #
    # 1 - keyword and positional parameter
    # 2 - token that denotes the following parameters as kw-only
    # 3 - keyword-only parameter
    pass
