# two ways to create an empty list
my_list = []
my_list = list()  # call to the a method, so you need round parentheses

# examples of lists
my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_list3 = ["a", 1, "Python", 5]

# create a nested list
my_nested_list = [my_list, my_list2]

# combine / extend a list
combo_list = []
one_list = [4, 5]
combo_list.extend(one_list) # add what is the one_list to combo_list
print(combo_list)  # [4, 5]

# or just concatenate the lists together (as you ar doing with strings)
my_list = [1, 2, 3]
print(type(my_list))
my_list2 = ["a", "b", "c"]
print(type(my_list2))
combo_list = my_list + my_list2
print(combo_list)  # [1, 2, 3, 'a', 'b', 'c']
print(type(combo_list))

# sort a list (in place)
alpha_list = [34, 23, 67, 100, 88, 2]
alpha_list.sort()
print(alpha_list)  # sorted alpha_list [2, 23, 34, 67, 88, 100]

# finding a logic error
alpha_list = [34, 23, 67, 100, 88, 2]
sorted_list = alpha_list.sort()
# the sort method returns a None object as lists sort in-place
print(sorted_list) # None