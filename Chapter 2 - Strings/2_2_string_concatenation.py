# the following demonstrates how to join two strings
string_one = "My dog ate "
string_two = "my homework!"
string_three = string_one + string_two


# we can go further on
string_three = string_one + "   " + string_two
print("string_three:", string_three)

string_three = string_one + ' / ' + string_two
print("string_three:", string_three)

#run & learn

'''
string_three: My dog ate    my homework!
string_three: My dog ate  / my homework!
'''