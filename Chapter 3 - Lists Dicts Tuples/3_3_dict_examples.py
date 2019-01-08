# there are two ways to create a Python dictionary (dict)
my_dict = {}
another_dict = dict() #by constructor

# here's an example with the dict containing data
my_other_dict = {"one": 1, "two": 2, "three": 3}

# add a new key
my_other_dict["four"] = 4
print(my_other_dict)

my_other_dict.pop("four")
print(my_other_dict)

# access values in a dict
my_other_dict["one"]
my_dict = {"name": "Mike", "address": "123 Happy Way"}

one_dict = {"one": 1}
two_dict = {"two": 2}
one_dict.update( two_dict)
print(one_dict)


# check if a dict has a particular key
"name" in my_dict  # returns True
print("name" in my_dict)
"state" in my_dict  # returns False

# get a view of the keys in a dict
my_dict.keys()
print(my_dict.keys())
print(my_dict.values())

'''
{'three': 3, 'four': 4, 'one': 1, 'two': 2}
{'three': 3, 'one': 1, 'two': 2}
{'one': 1, 'two': 2}
True
dict_keys(['name', 'address'])
dict_values(['Mike', '123 Happy Way'])
'''