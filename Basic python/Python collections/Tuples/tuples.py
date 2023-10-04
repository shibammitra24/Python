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

# accessing items in a tuple:
items = ("bag", "bottle", "car_keys", "phone")
print(items)
print(items[0]) # positive indexing
print(items[-2]) # negative indexing
print(items[1:4]) # range indexing
print(items[-2:]) # negative range indexing

# check if an item is in a tuple
if "bottle" in items:
    print("IS PRESENT")