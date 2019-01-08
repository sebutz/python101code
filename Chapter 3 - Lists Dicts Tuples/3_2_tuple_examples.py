# a few tuple examples
# to be a tuple(has to have at least 2 values)

my_tuple = (1, 2, 3, 4, 5)
my_tuple[0:3]  # tuple slicing as in strings

another_tuple = tuple()  # creating an empty tuple
print(another_tuple) # empty tuple

my_tuple2 = (1, "223", 23.0, "abs")
print(my_tuple2[:])

another_tuple += my_tuple2[:] # adding whole tuple
print(another_tuple)

# nested tuples
some_tuple = (another_tuple, "abc")
print(some_tuple)

# add to a tuple another tuple
some_tuple += (0, 2, "abc")
print(some_tuple)

# list -> tuple (pass to the tuple constructor)
# turn a list into a tuple via casting
abc = tuple([1, 2, 3])


# now we can solve the problem adding just one value

bcd = tuple([1])
print(bcd)

print(type(bcd))

'''
()
(1, '223', 23.0, 'abs')
(1, '223', 23.0, 'abs')
((1, '223', 23.0, 'abs'), 'abc')
((1, '223', 23.0, 'abs'), 'abc', 0, 2, 'abc')
(1,)
<class 'tuple'>
'''