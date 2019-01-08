# a simple if statement
if 2 > 1:
    print("This is a True statement!")

# another simple  if statement
var1 = 1
var2 = 3
if var1 < var2:
    print("This is also True")

# some else
if var1 > var2:
    print("This should not be printed")
else:
    print("Ok, that's the good branch")


# -1 -----0 -------1
if var1 < -1:
    print("not reachable")
elif var1 <  0:
    print("not reachable also")
elif var1 < 1:
    print("almost there")
else:
    print("at last")


if var1 < -1:
    print("not reachable")
elif var1 <  0:
    print("not reachable also")
elif var1 <= 1:
    print("right there")
else:
    print("not reachable ")

# let's make it dynamic

user_says = input("give a price:")

user_says_int = int(user_says)

#simplified
if 0 < user_says_int <= 10:
    print("you got the right price, boss")
elif 10 < user_says_int <= 20:
    print("that's a lot")
elif user_says_int >= 20:
    print("are you nuts?")
else:
    print("what?")

# and, or, not
if (user_says_int > 0 and
        user_says_int <= 10):
    print("good price")
elif user_says_int > 10 and user_says_int < 20:
    print("that's a lot")
elif user_says_int >= 20:
    print("are you nuts?")
else:
    print("what?")

if not False:
    print("ola")

x = 4
if x != 2:
    print("boom")
else:
    print("kboom")

# in list checking
my_list = [1, 2, 3, 4]
x = 10
if x in my_list :
    print("gotcha")
else:
    print("keep looking")

# checking for Nothing
# different types (they are evaluated differently !!!!)
empty_list = []
empty_map = {}
empty_string = ""
nothing = None
# for ex:
print(empty_list == None) # False


if empty_list == []:
    print("empty list")
else:
    print("something")

# same as
if empty_list:
    print(empty_list)
else:
    print("something")


if not empty_list:
    print("something")
else:
    print("empty")

if not nothing:
    print("some value exists")
else:
    print("absolutely nothing")



'''
# execute this code only if this program is executed as standlone file
if __name__ == "__main__":
    #whatever
'''


