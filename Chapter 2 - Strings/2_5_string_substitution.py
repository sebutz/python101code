# string substitution
# or substitution

# the old way
# $ is the substitution sign (to be inserted soon)
my_string = "I like %s" % "Python"
print( my_string) #I like Python

var = "cookies"
newString = "I like %s" % var
newString
print(newString) #I like cookies

another_string = "I like %s and %s" % ("Python", var)
print(another_string) #I like Python and cookies

# you have to be very specific with what to insert
# this will cause a TypeError
# another_string = "I like %s and %s" % "Python"

# this will work
another_string = "I like %s and %s" % ("Python", "Python")
print(another_string) #I like Python and Python

# string formatting
my_string = "%i + %i = %i" % (1,2,3)
print(my_string)

float_string = "%f" % (1.23)
float_string

float_string2 = "%.2f" % (1.23)
float_string2

float_string3 = "%.2f" % (1.237)
float_string3

# passing bad data raises a TypeError
#int_float_err = "%i + %f" % ("1", "2.00")

# did you spot the error, then fix
int_float = "%i + %f" % (1, 2.00)
print(int_float)

# this is bad too
#int_float_err = "%i + %f" % (1, "2.00")


# ---------------------------------------------
# new style of string substitution / formatting
# pay attention to the syntax: the type is after the paranthesis %(value_to_be_inserted)type_of_value
print("%(lang)s is fun!" % {"lang":"Python"}) # too verbose?
# the advantage is that you can reuse the same value to be imserted
print("%(value)s %(value)s %(value)s !" % {"value":"SPAM"})

# this one won't work!
# print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2})

# this is a fix of the previous example
print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2, "z":3})

# messing with the order of substitution
# another variant, without telling the type
py = "Python is as simple as {0}, {1}, {2}".format("a", "b", "c")
print(py)
py = "Python is as simple as {1}, {0}, {2}".format("a", "b", "c")
print(py)

# careless without type
py = "Python is as simple as {0}, {1}".format(2, 0.3)
print(py)

# doing the substitution from a map (dictionary)
# creating the dict and then doing the substitution by the name of the dictionary
dick = {"x": 0, "y": 10, "z": 300}
print("Graph a point at where x={x} and y={y}".format(**dick))

# if the key is missing we have an error : KeyError: 't'
dick = {"x": 0, "y": 10, "z": 300}
# print("Graph a point at where x={x} and t={t}".format(**dick))
