# adding arguments
def add(a, b):
    return a + b

# call the function with arguments
add(1, 2)

# call the function with the wrong number of arguments
try:
    add(1)  # causes a TypeError
except TypeError:
    print("wrong nr. of argument ")


# call the function with keyword arguments
# named arguments
add(a=2, b=3)


# assign the result to a variable
total = add(b=4, a=5)
print(total)

# deefault arguments
def add2(a = 2, b = 3):
    return a + b

print(add2())
print(add2(10))
