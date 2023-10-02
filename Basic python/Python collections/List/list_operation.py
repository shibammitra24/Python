lst1 = [15, 25, 35, 45, 55]
lst2 = [100, 150]

# append
lst1.append(60)
print(lst1)

# insert
lst1.insert(4, 75)
print(lst1)

# extend
lst1.extend(lst2)
print(lst1)

# remove
lst1.remove(35)
print(lst1)

# pop
lst1.pop() # we can give the index value to remove from the list
print(lst1)