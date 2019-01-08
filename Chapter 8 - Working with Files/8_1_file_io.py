# open a file that is in the same folder as this script
# default mode: read-only
handle = open("test.txt")
print(handle)
handle.close()

# open a file by specifying its path
# you have to specify the path using raw string, r"path"
try:
   handle = open(r"some path", "r")  # explicit read only mode (raw_string, "r")
except IOError:
   print("cannot open that")


# open the file in read-only binary mode
handle = open("test.txt", "rb")
print(handle)


# let's read it

data = handle.read()
print(data) # b'This is a test file\nline 2\nline 3\nthis line intentionally left blank'
handle.close()


handle_text = open("test.txt", "r")
data  = handle_text.readline()  # read the first line
handle_text.close()
print(data)

handle_text = open("test.txt", "r")
data_all = handle_text.readlines()   # all the lines in a list
handle_text.close()
print(data_all) # ['This is a test file\n', 'line 2\n', 'line 3\n', 'this line intentionally left blank']


'''
<_io.TextIOWrapper name='test.txt' mode='r' encoding='US-ASCII'>
cannot open that
<_io.BufferedReader name='test.txt'>
b'This is a test file\nline 2\nline 3\nthis line intentionally left blank'
This is a test file

['This is a test file\n', 'line 2\n', 'line 3\n', 'this line intentionally left blank']
'''