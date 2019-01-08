handle = open("test.txt", "r")
# iterate over the handle, which is cool
for line in handle:
    print(line)
handle.close()

'''
This is a test file

line 2

line 3

this line intentionally left blank

Process finished with exit code 0
'''