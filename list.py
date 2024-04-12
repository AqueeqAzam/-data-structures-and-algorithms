# Traversing: accessing elements of list at once
list = [23, 45, 'tyson', 3.14]
for i in list:
  print(i, end=", ")

# appending: add elements at end of list
list = [23, 45, 'tyson', 3.14]
list.append(98)
for x in list:
  print(x, end=", ")

# insertion: add elements at specific position
list = [23, 45, 'tyson', 3.14]
list.insert(2, 50)
for x in list:
  print(x)

# pop: removing elements at specific position
list = [23, 45, 'tyson', 3.14]
list.pop(2)
for x in list:
  print(x)

# remove: remove item at specific value
list = [23, 45, 'tyson', 3.14]
list.remove(45)
for x in list:
  print(x)

# merging: combing two list
list1 = [34, 56, 8, 7, 23]
list2 = [21, 34, 65, 34, 4]
joinlist = list1 + list2
print(joinlist)

# Sorting: arranging elements of list
list = [34, 45, 65, 2, 23, 43, 12, 90, 3]
list.sort()
for i in list:
  print(i, end = ' ')
