# a simple list comprehension
# just an one line for loop that produces a Python list data structure
x = [i for i in range(5)]
print(x)

# turn a list of strings into a list of ints
x = ['1', '2', '3', '4', '5']
y = [int(i) for i in x]

myStringList = [" abc", "    dcf", "efr"]

# strip off all the leading or ending white space
myStrings = [s.strip() for s in myStringList]
print(myStrings)

# how to turn a list of lists into one list (flattening)
vec = [[1,2,3], [4,5,6], [7,8,9]]
flat_vec = [num for elem in vec for num in elem]  # just like 2 for , just follow up the num
flatty = [num for num in vec]
print(flatty) # printing the vec
print(flatty == vec) # True
print(flat_vec)

# a simple dict comprehension
print( {i: str(i) for i in range(5)} ) # just follow the construction {i: str(i) ....  }
# and then ask yourself where is i coming from: for i in ...

# swapping keys and values with a dict comprehension
# work only if the dictionary values are immutable such as strings
my_dict = {1: "dog", 2: "cat", 3: "hamster"}
print( {value: key for key, value in my_dict.items()} ) # key is inferred
# just follow the construction {value: key} for key, value in ... should be the pairs aka my_dict.items()
# where are the value, key are coming from

# turn a list into a set using a set comprehension
# something like eliminate the non-distincts from a list
my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
my_set = {x for x in my_list}   # set
print(my_set)
print(type(my_set))