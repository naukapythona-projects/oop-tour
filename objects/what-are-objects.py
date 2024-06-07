# Basic properties of all objects
## STATE: Size, shape, colour, weight/mass, animate/inanimate, elegance
## METHODS: Contain things, protect things

## Specific example: Atom
### STATE: A specific number of electrons and nucleus - a specific number of neutrons and protons
### METHODS: Give and receive electrons, bond with other atoms

# State and methods operating on state are basic building blocks of objects.
# Methods often mutate state.

# In Computer Science objects have a place in memory.
# Specifically in Python, whether objects exist or not depends on reference count.
from weakref import ref

class MyObject:
    pass

a = b = MyObject()  # 2 references to an object at ...
wref = ref(a)  # weak reference to the same object
print(wref)
del a, b  # delete the 2 references
print(wref)

# Every objects has a certain amount of references.
# If the amount of references to an object hits zero, the object stops existing.

# Summary
# Objects are structures characterized by states and methods that operate on these states.
# For example, atom's state is the number of electrons, protons and neutrons.
# Atom's methods could be to add or remove an electron.
#
# object = state + methods
#
# In Python, every object has a place in memory (id() in CPython) and references to it.