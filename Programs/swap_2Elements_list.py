list = [23, 65, 19, 90]
print(list)
temp = list[0]
list[0] = list[2]
list[2] = temp
print(list)

list2 = [1, 2, 3, 4, 5]
print(list2)
temp1 = list2[1]
list2[1] = list2[4]
list2[4] = temp1
print(list2)