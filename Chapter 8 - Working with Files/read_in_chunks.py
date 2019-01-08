# primitive way of reading in chunks
handle = open("test.txt", "r")
while True:
    data = handle.read(1024)  # that's 1 Kb
    print(data)
    if not data:  # stop reading when there is no data, otherwise
        break

''''
This is a test file
line 2
line 3
this line intentionally left blank
'''