# list comprehension in python

# using for loop:
lst = [14, 58, 61, 21, 11]
# new_lst = []

# for i in lst:
#     if i>20:
#         new_lst.append(i)

# print(new_lst)

# using list comprehension:
new_lst = [i for i in lst if i>20]
print(new_lst)