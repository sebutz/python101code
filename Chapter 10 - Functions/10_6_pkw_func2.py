def mixed_function(a, b=2, c=3):
    return a+b+c

# call the function with one argument and 2 keyword arguments
res1 = mixed_function(1, b=4, c=5)
print(res1)
# call the argument with just the required argument
res2 = mixed_function(1) # b =2, c = 3
print(res2)
