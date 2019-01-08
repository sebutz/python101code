# built-in


list = range(1, 10, 2)
print(type(list))  # range

# a basic for loop
for number in range(5):
    print(number)
    
# you can also write the above like this
for number in [0, 1, 2, 3, 4]:
    print(number)
    
# this is how to loop over the keys in a dict
a_dict = {"one": 1, "two": 2, "three": 3}
for key in a_dict:
    print(key)
    
# sort the keys before looping over them
a_dict = {5: "five",  4: "four", 1: "one", 2: "two", 3: "three"}
keys = a_dict.keys()  # set and it will order the keys
print("the keys", keys)

# no need to sort the keys in this case
sorted(keys)  # only if the key are from the same type at least
print("the keys", keys)

'''
the keys dict_keys([1, 2, 3, 4, 5])
the keys dict_keys([1, 2, 3, 4, 5])
'''

for key in keys:
    print(key)


b_dict = {"c":  345, "a": 123, "b": 234}

keys = b_dict.keys()
print("keys", keys)  # keys dict_keys(['c', 'a', 'b'])
sorted(keys) # will not sort the keys
print("keys", keys)
'''
keys dict_keys(['c', 'a', 'b'])
keys dict_keys(['c', 'a', 'b'])
'''

# Let's use a conditional to print out only even numbers
for number in range(10):
    if number % 2 == 0:
        print(number)
        
# using the else statement with for
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    if i == 3:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")



my_list = [1, 2, 3, 4, 5]

# if the for loop completed successfully
# then else of the for gets executed
# otherwise no: the break will break out of the for-else (will skip the else also)
for i in my_list:
    if i == 6:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")