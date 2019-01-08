# infinite number of arguments
# infinite number of keyword arguments
def many(*args, **kwargs):
    print(args) # list
    print(kwargs)  # dictionary
    
res = many(1, 2, 3, name="Mike", job="programmer")
print("result:", res)

'''
(1, 2, 3)
{'name': 'Mike', 'job': 'programmer'}
result: None

'''
