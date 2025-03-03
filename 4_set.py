# 📌 1. Creating a Set
fruits = {"🍎", "🍌", "🍊", "🍇"}
print("🌟 Initial Set:", fruits)


# 📌 2. Adding Elements
print("\n➕ Adding Elements:")
fruits.add("🍉")  # Add a single element
print("✅ After Adding 🍉:", fruits)

fruits.update(["🍒", "🍍"])  # Add multiple elements
print("✅ After Adding Multiple Fruits:", fruits)


# 📌 3. Removing Elements
print("\n❌ Removing Elements:")
fruits.remove("🍌")  # Remove an element (raises KeyError if not found)
print("✅ After Removing 🍌:", fruits)

fruits.discard("🍍")  # Remove an element (does not raise an error if not found)
print("✅ After Discarding 🍍:", fruits)

popped_fruit = fruits.pop()  # Remove and return an arbitrary element
print("✅ Popped Fruit:", popped_fruit)
print("✅ After Popping:", fruits)


# 📌 4. Checking Membership
print("\n🧐 Checking Membership:")
print("Is 🍎 in the set?", "🍎" in fruits)  # True
print("Is 🍉 in the set?", "🍉" in fruits)  # False


# 📌 5. Iterating Over a Set
print("\n🚶‍♂️ Iterating Over the Set:")
for fruit in fruits:
    print(fruit, end=", ")


# 📌 6. Set Operations (Union, Intersection, Difference, Symmetric Difference)
set1 = {"🍎", "🍌", "🍊"}
set2 = {"🍊", "🍇", "🍉"}

print("\n\n🔗 Set Operations:")
union_set = set1.union(set2)  # All unique elements from both sets
print("Union:", union_set)

intersection_set = set1.intersection(set2)  # Common elements in both sets
print("Intersection:", intersection_set)

difference_set = set1.difference(set2)  # Elements in set1 but not in set2
print("Difference (set1 - set2):", difference_set)

symmetric_difference_set = set1.symmetric_difference(set2)  # Elements in either set but not both
print("Symmetric Difference:", symmetric_difference_set)


# 📌 7. Checking Subset and Superset
subset = {"🍊", "🍇"}
superset = {"🍎", "🍌", "🍊", "🍇", "🍉"}

print("\n🔍 Checking Subset and Superset:")
print("Is subset a subset of superset?", subset.issubset(superset))  # True
print("Is superset a superset of subset?", superset.issuperset(subset))  # True


# 📌 8. Clearing a Set
fruits.clear()
print("\n🧹 After Clearing the Set:", fruits)


# 📌 9. Frozen Sets (Immutable Sets)
frozen_fruits = frozenset({"🍎", "🍌", "🍊"})
print("\n🧊 Frozen Set:", frozen_fruits)

# Attempting to modify a frozen set (will raise an error)
try:
    frozen_fruits.add("🍉")  # ❌ AttributeError: 'frozenset' object has no attribute 'add'
except AttributeError as e:
    print("❌ Error:", e)


# 📌 10. Set Comprehension
squares = {x**2 for x in range(1, 6)}
print("\n🔢 Set Comprehension (Squares):", squares)


# 📌 11. Converting Between Lists and Sets
fruit_list = ["🍎", "🍌", "🍊", "🍎", "🍌"]
unique_fruits = set(fruit_list)  # Convert list to set to remove duplicates
print("\n🔄 List to Set:", unique_fruits)

back_to_list = list(unique_fruits)  # Convert set back to list
print("🔄 Set to List:", back_to_list)


# 📌 12. Length of a Set
print("\n📏 Length of the Set:", len(unique_fruits))


# 📌 13. Copying a Set
copied_set = unique_fruits.copy()
print("\n📋 Copied Set:", copied_set)



#--------------------Expected Output-----------------------
🌟 Initial Set: {'🍊', '🍇', '🍎', '🍌'}

➕ Adding Elements:
✅ After Adding 🍉: {'🍊', '🍇', '🍎', '🍉', '🍌'}
✅ After Adding Multiple Fruits: {'🍊', '🍇', '🍎', '🍉', '🍒', '🍍', '🍌'}

❌ Removing Elements:
✅ After Removing 🍌: {'🍊', '🍇', '🍎', '🍉', '🍒', '🍍'}
✅ After Discarding 🍍: {'🍊', '🍇', '🍎', '🍉', '🍒'}
✅ Popped Fruit: 🍊
✅ After Popping: {'🍇', '🍎', '🍉', '🍒'}

🧐 Checking Membership:
Is 🍎 in the set? True
Is 🍉 in the set? True

🚶‍♂️ Iterating Over the Set:
🍇, 🍎, 🍉, 🍒, 

🔗 Set Operations:
Union: {'🍇', '🍎', '🍉', '🍒', '🍊'}
Intersection: {'🍊'}
Difference (set1 - set2): {'🍎', '🍌'}
Symmetric Difference: {'🍎', '🍉', '🍇', '🍌'}

🔍 Checking Subset and Superset:
Is subset a subset of superset? True
Is superset a superset of subset? True

🧹 After Clearing the Set: set()

🧊 Frozen Set: frozenset({'🍊', '🍇', '🍎'})
❌ Error: 'frozenset' object has no attribute 'add'

🔢 Set Comprehension (Squares): {1, 4, 9, 16, 25}

🔄 List to Set: {'🍊', '🍇', '🍎', '🍌'}
🔄 Set to List: ['🍊', '🍇', '🍎', '🍌']

📏 Length of the Set: 4

📋 Copied Set: {'🍊', '🍇', '🍎', '🍌'}
