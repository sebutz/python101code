#modules
import math

print(math.sqrt(4))
# we need to write also the library


# no need
from math import sqrt
print(sqrt(9))


# BAD : shadowing: we change the function sqrt into a variable
sqrt = 9
print(sqrt)

# import what you need only and not pollute the namespace with all kind of names you don't know
