# string slicing
my_string = "I like Python!"


# just the first character but not included the second char
# 0 --> string length len(my_string) - 1
print("string length:", len(my_string))

print(my_string[0:1])

#same as
my_string[:1]
print(my_string[:1])

my_string[0:12]

my_string[0:13]
print(my_string[0:13])

my_string[0:14]
print(my_string[0:14]) # full string

print(my_string[0: len(my_string)])

my_string[0:-5]
print(my_string[0:-5]) # starts with 0 but end 5 characters before ending

#same as
print(my_string[0: len(my_string) - 5])
print(my_string[0: 14 - 5])

# full
my_string[:]
print(my_string[:])

#starting with the 3rd char(0, 1, 2) until the end
my_string[2:]
print(my_string[2:])

# string indexing
print(my_string[0])  # prints the first character of the string

'''
string length: 14
I
I
I like Python
I like Python!
I like Python!
I like Py
I like Py
I like Py
I like Python!
like Python!
I
'''