# open and read the file using the with operator
# simplifying the reading and writing

# with creates a CONTEXT MANAGER :
# automatically closes the file for you when you are done processing
with open("test.txt") as file_handler:
    for line in file_handler:
        print(len(line))
        print(line)
# no need to close
# you can do all the I/O ops as long as you are in the with block
# after the ops are done and you are out of the with block then the file handler closes.


# weird syntax
