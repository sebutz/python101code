# this script demonstrates how to use a global
# to fic the scope issue in 10_7_scope.py

def function_a():
    global a # here
    a = 1
    b = 2
    return a + b

def function_b():
    c = 3
    return a + c

print(function_a())
print(function_b())
