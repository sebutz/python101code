# open a file in read-only mode
handle = open("test.txt", "r")
# read the data with the handler
data = handle.read()
# print it out
print(data)
print(type(data)) # str
# close the file
handle.close()


