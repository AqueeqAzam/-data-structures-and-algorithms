# 📌 1. Append, Insert, Delete, and Remove Elements
fruits = ["🍎", "🍌", "🍊", "🍇"]
print("Initial List:", fruits)

# Append 🍉 at the end
fruits.append("🍉")
print("After Append 🍉:", fruits)

# Insert 🍒 at index 2
fruits.insert(2, "🍒")
print("After Insert 🍒 at index 2:", fruits)

# Remove 🍌
fruits.remove("🍌")
print("After Remove 🍌:", fruits)


# 📌 2. Reverse and Sort a List
numbers = [10, 5, 8, 3, 2]
print("\nOriginal Numbers:", numbers)

# Reverse the list
numbers.reverse()
print("After Reverse:", numbers)

# Sort the list
numbers.sort()
print("After Sorting:", numbers)


# 📌 3. Find Unique Values and Indexes
nums = [5, 3, 5, 2, 3, 1, 4, 1]
print("\nOriginal List:", nums)

# Unique values
unique_values = list(set(nums))
print("Unique Values:", unique_values)

# Indices of unique values
indices = [nums.index(i) for i in unique_values]
print("Indices of Unique Values:", indices)


# 📌 4. Find Max and Min in a List
numbers = [10, 20, 30, 40, 50]
print("\nNumbers List:", numbers)

max_value = max(numbers)
min_value = min(numbers)

print("Max Value:", max_value)
print("Min Value:", min_value)


# 📌 5. Traversing a List (Accessing Elements)
data = [23, 45, 'tyson', 3.14]
print("\nTraversing the List:", end=" ")
for item in data:
    print(item, end=", ")


# 📌 6. Appending and Inserting Elements
data.append(98)
print("\nAfter Append 98:", data)

data.insert(2, 50)
print("After Insert 50 at index 2:", data)


# 📌 7. Removing Elements by Index or Value
data.pop(2)  # Removes element at index 2
print("After Pop at index 2:", data)

data.remove(45)  # Removes the first occurrence of 45
print("After Remove 45:", data)


# 📌 8. Merging Two Lists
list1 = [34, 56, 8, 7, 23]
list2 = [21, 34, 65, 34, 4]
merged_list = list1 + list2
print("\nMerged List:", merged_list)


# 📌 9. Sorting a List
unsorted_list = [34, 45, 65, 2, 23, 43, 12, 90, 3]
unsorted_list.sort()
print("Sorted List:", unsorted_list)


# 📌 10. Slicing a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nOriginal List:", numbers)

print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[-5:])
print("Middle elements:", numbers[2:7])
print("Every 2nd element:", numbers[::2])


# 📌 11. List Comprehension (Creating a New List)
squares = [x**2 for x in range(1, 11)]
print("\nList of Squares (1-10):", squares)


# 📌 12. Copying a List (Shallow Copy)
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print("\nCopied List:", copied_list)


# 📌 13. Extending a List (Adding Another List to It)
list1 = [10, 20, 30]
list2 = [40, 50, 60]
list1.extend(list2)
print("After Extending List1 with List2:", list1)


# 📌 14. Finding an Element in a List
items = ["apple", "banana", "cherry"]
index = items.index("banana")
print("\nIndex of 'banana':", index)


# 📌 15. Counting Occurrences of an Element
nums = [1, 2, 3, 1, 2, 1, 4, 5]
count_ones = nums.count(1)
print("Count of 1 in List:", count_ones)


# 📌 16. Clearing a List (Removing All Elements)
nums.clear()
print("After Clearing List:", nums)


# 📌 17. Checking Membership in a List
fruits = ["🍎", "🍌", "🍊", "🍇"]
print("\nIs 🍎 in list?", "🍎" in fruits)
print("Is 🍉 in list?", "🍉" in fruits)

#---------------Expected Output-----------------------

Initial List: ['🍎', '🍌', '🍊', '🍇']
After Append 🍉: ['🍎', '🍌', '🍊', '🍇', '🍉']
After Insert 🍒 at index 2: ['🍎', '🍌', '🍒', '🍊', '🍇', '🍉']
After Remove 🍌: ['🍎', '🍒', '🍊', '🍇', '🍉']

Original Numbers: [10, 5, 8, 3, 2]
After Reverse: [2, 3, 8, 5, 10]
After Sorting: [2, 3, 5, 8, 10]

Original List: [5, 3, 5, 2, 3, 1, 4, 1]
Unique Values: [1, 2, 3, 4, 5]
Indices of Unique Values: [5, 3, 1, 6, 0]

Max Value: 50
Min Value: 10

Traversing the List: 23, 45, tyson, 3.14, 
After Append 98: [23, 45, 'tyson', 3.14, 98]
After Insert 50 at index 2: [23, 45, 50, 'tyson', 3.14, 98]

Merged List: [34, 56, 8, 7, 23, 21, 34, 65, 34, 4]

Sorted List: [2, 3, 12, 23, 34, 43, 45, 65, 90]

First 5 elements: [1, 2, 3, 4, 5]
Last 5 elements: [6, 7, 8, 9, 10]
Middle elements: [3, 4, 5, 6, 7]
Every 2nd element: [1, 3, 5, 7, 9]

List of Squares (1-10): [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Copied List: [1, 2, 3, 4, 5]

After Extending List1 with List2: [10, 20, 30, 40, 50, 60]

Index of 'banana': 1

Count of 1 in List: 3

After Clearing List: []

Is 🍎 in list? True
Is 🍉 in list? False

