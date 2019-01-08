# catching errors the old school way
try:
    file_handler = open("test.txt")
    for line in file_handler:
        print(line)
except IOError:
    print("An IOError has occurred!")
finally:
    file_handler.close()  # exactly : we need to take care of closing the handler anyway
    
# catching errors when using the with operator
# no need to close the handler anyway, so we don't need the finally for that
try:
    with open("test.txt") as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print("An IOError has occurred!")