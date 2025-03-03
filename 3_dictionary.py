# 📌 1. Creating a Dictionary
fruits = {
    "apple": "🍎",
    "banana": "🍌",
    "orange": "🍊",
    "grape": "🍇"
}
print("🌟 Initial Dictionary:", fruits)


# 📌 2. Accessing Values
print("\n🔍 Accessing Values:")
print("✅ Value of 'apple':", fruits["apple"])
print("✅ Value of 'banana':", fruits.get("banana"))


# 📌 3. Adding or Updating Key-Value Pairs
print("\n➕ Adding or Updating Key-Value Pairs:")
fruits["watermelon"] = "🍉"  # Add a new key-value pair
fruits["banana"] = "🍌🍌"     # Update an existing key
print("✅ After Adding/Updating:", fruits)


# 📌 4. Removing Key-Value Pairs
print("\n❌ Removing Key-Value Pairs:")
removed_value = fruits.pop("orange")  # Remove by key and return the value
print("✅ Removed 'orange':", removed_value)
print("✅ After Removing:", fruits)

del fruits["grape"]  # Delete a key-value pair directly
print("✅ After Deleting 'grape':", fruits)


# 📌 5. Iterating Over a Dictionary
print("\n🚶‍♂️ Iterating Over the Dictionary:")
print("✅ Keys:")
for key in fruits.keys():
    print(key, end=", ")

print("\n✅ Values:")
for value in fruits.values():
    print(value, end=", ")

print("\n✅ Key-Value Pairs:")
for key, value in fruits.items():
    print(f"{key}: {value}")


# 📌 6. Membership Testing
print("\n🧐 Membership Testing:")
print("Is 'apple' in the dictionary?", "apple" in fruits)  # Check for key
print("Is 'cherry' in the dictionary?", "cherry" in fruits)


# 📌 7. Merging Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}  # Merge using unpacking
print("\n🔗 Merged Dictionary:", merged_dict)


# 📌 8. Dictionary Comprehension
squares = {x: x**2 for x in range(1, 6)}
print("\n🔢 Dictionary Comprehension (Squares):", squares)


# 📌 9. Nested Dictionaries
nested_dict = {
    "fruits": {"apple": "🍎", "banana": "🍌"},
    "numbers": {"one": 1, "two": 2}
}
print("\n📦 Nested Dictionary:", nested_dict)

# Accessing nested values
print("✅ Value of 'apple':", nested_dict["fruits"]["apple"])
print("✅ Value of 'two':", nested_dict["numbers"]["two"])


# 📌 10. Default Values with `get()`
print("\n❓ Using `get()` with Default Values:")
print("Value of 'cherry':", fruits.get("cherry", "🍒 (default)"))


# 📌 11. Clearing a Dictionary
fruits.clear()
print("\n🧹 After Clearing the Dictionary:", fruits)


# 📌 12. Copying a Dictionary
original_dict = {"a": 1, "b": 2}
copied_dict = original_dict.copy()
print("\n📋 Copied Dictionary:", copied_dict)


# 📌 13. Sorting a Dictionary
unsorted_dict = {"b": 2, "a": 1, "c": 3}
sorted_dict = dict(sorted(unsorted_dict.items()))
print("\n📈 Sorted Dictionary:", sorted_dict)


# 📌 14. Using `setdefault()` to Add Default Values
person = {"name": "Alice", "age": 30}
person.setdefault("profession", "Engineer")  # Adds if key doesn't exist
person.setdefault("age", 35)  # Does nothing since 'age' exists
print("\n👤 Dictionary After `setdefault()`:", person)


# 📌 15. Dictionary Views
print("\n👀 Dictionary Views:")
keys_view = person.keys()
values_view = person.values()
items_view = person.items()

print("Keys View:", keys_view)
print("Values View:", values_view)
print("Items View:", items_view)



#-----------------Expected Output-------------------------
🌟 Initial Dictionary: {'apple': '🍎', 'banana': '🍌', 'orange': '🍊', 'grape': '🍇'}

🔍 Accessing Values:
✅ Value of 'apple': 🍎
✅ Value of 'banana': 🍌

➕ Adding or Updating Key-Value Pairs:
✅ After Adding/Updating: {'apple': '🍎', 'banana': '🍌🍌', 'orange': '🍊', 'grape': '🍇', 'watermelon': '🍉'}

❌ Removing Key-Value Pairs:
✅ Removed 'orange': 🍊
✅ After Removing: {'apple': '🍎', 'banana': '🍌🍌', 'grape': '🍇', 'watermelon': '🍉'}
✅ After Deleting 'grape': {'apple': '🍎', 'banana': '🍌🍌', 'watermelon': '🍉'}

🚶‍♂️ Iterating Over the Dictionary:
✅ Keys:
apple, banana, watermelon, 
✅ Values:
🍎, 🍌🍌, 🍉, 
✅ Key-Value Pairs:
apple: 🍎
banana: 🍌🍌
watermelon: 🍉

🧐 Membership Testing:
Is 'apple' in the dictionary? True
Is 'cherry' in the dictionary? False

🔗 Merged Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

🔢 Dictionary Comprehension (Squares): {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

📦 Nested Dictionary: {'fruits': {'apple': '🍎', 'banana': '🍌'}, 'numbers': {'one': 1, 'two': 2}}
✅ Value of 'apple': 🍎
✅ Value of 'two': 2

❓ Using `get()` with Default Values:
Value of 'cherry': 🍒 (default)

🧹 After Clearing the Dictionary: {}

📋 Copied Dictionary: {'a': 1, 'b': 2}

📈 Sorted Dictionary: {'a': 1, 'b': 2, 'c': 3}

👤 Dictionary After `setdefault()`: {'name': 'Alice', 'age': 30, 'profession': 'Engineer'}

👀 Dictionary Views:
Keys View: dict_keys(['name', 'age', 'profession'])
Values View: dict_values(['Alice', 30, 'Engineer'])
Items View: dict_items([('name', 'Alice'), ('age', 30), ('profession', 'Engineer')])
