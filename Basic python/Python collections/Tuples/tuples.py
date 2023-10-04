colors = ("blue", "green", "violet", "red")
print(colors)

# check the type
print(type(colors))

# create tuple with 1 item:
# tup = ("computer") # it will be identified as string
# print(type(tup))
# tup = ("computer",) # we have to put a "," after the value to take it as a tuple
# print(type(tup))
# we can also do this by typecasting:
tup = tuple(("computer"))
print(type(tup))

# check the length of tuple
print(len(colors))
print(len(tup))