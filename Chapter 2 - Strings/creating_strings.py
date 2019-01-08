# The following shows different methods of creating a string

##
#
##

my_string = "Welcome to Python!"
another_string = 'The bright red fox jumped the fence.'
a_long_string = '''This is a
multi-line string. It covers more than
one line'''


print(a_long_string)
# Q: this set of strings shows how to mix single and double-quotes
# A: mixing & nesting the different quotes
my_string = "I'm a Python programmer!"
otherString = 'The word "python" usually refers to a snake'
tripleString = """Here's another way to embed "quotes" in a string"""

# cast an integer to a string using Python's str() class
my_number = 123
my_string = str(my_number)

print(my_number)
print(my_string)
# A: you can pass different types to print, without worrying
print(123, "aaaa", 34.0)