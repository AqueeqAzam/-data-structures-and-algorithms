# 📌 1. Accessing Elements
fruits = ("🍎", "🍌", "🍊", "🍇")
print("🌟 Initial Tuple:", fruits)

# Access first and last elements
print("✅ First fruit:", fruits[0])
print("✅ Last fruit:", fruits[-1])


# 📌 2. Slicing
numbers = (1, 2, 3, 4, 5)
print("\n✂️ Original Tuple:", numbers)

# Slice first 3 elements
print("➡️ First 3 elements:", numbers[:3])

# Slice last 2 elements
print("⬅️ Last 2 elements:", numbers[-2:])


# 📌 3. Iterating
data = (23, 45, 'tyson', 3.14)
print("\n🚶‍♂️ Traversing the Tuple:", end=" ")
for item in data:
    print(item, end=", ")


# 📌 4. Membership Testing
fruits = ("🍎", "🍌", "🍊", "🍇")
print("\n\n🧐 Is 🍎 in tuple?", "🍎" in fruits)  # True
print("🧐 Is 🍉 in tuple?", "🍉" in fruits)  # False


# 📌 5. Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("\n🔗 Combined Tuple:", combined)


# 📌 6. Counting and Indexing
nums = (1, 2, 3, 1, 2, 1, 4, 5)
print("\n🧮 Count of 1:", nums.count(1))  # Output: 3
print("📍 Index of 4:", nums.index(4))  # Output: 6


# 📌 7. Unpacking
person = ("Alice", 30, "Engineer")
name, age, profession = person
print("\n👤 Name:", name)
print("📅 Age:", age)
print("🛠️ Profession:", profession)


# 📌 8. Adding an Element (Workaround)
fruits = ("🍎", "🍌", "🍊", "🍇")
new_fruits = fruits + ("🍉",)
print("\n✅ New Tuple After Adding 🍉:", new_fruits)


# 📌 9. Removing an Element (Workaround)
fruits = ("🍎", "🍌", "🍊", "🍇")
new_fruits = tuple(fruit for fruit in fruits if fruit != "🍌")
print("❌ New Tuple After Removing 🍌:", new_fruits)


# 📌 10. Replacing an Element (Workaround)
fruits = ("🍎", "🍌", "🍊", "🍇")
new_fruits = fruits[:1] + ("🍒",) + fruits[2:]
print("🔄 New Tuple After Replacing 🍌 with 🍒:", new_fruits)


# 📌 11. Nested Tuples
nested_tuple = (("🍎", "🍌"), ("🍊", "🍇"))
print("\n📦 Nested Tuple:", nested_tuple)

# Accessing elements in a nested tuple
print("✅ First element of first tuple:", nested_tuple[0][0])
print("✅ Second element of second tuple:", nested_tuple[1][1])


# 📌 12. Converting Between Lists and Tuples
fruits_list = ["🍎", "🍌", "🍊", "🍇"]
fruits_tuple = tuple(fruits_list)
print("\n🔄 List to Tuple:", fruits_tuple)

fruits_list_again = list(fruits_tuple)
print("🔄 Tuple to List:", fruits_list_again)


# 📌 13. Using Tuples as Dictionary Keys
coordinates = {("lat", "lon"): (37.7749, -122.4194)}
print("\n🗺️ Dictionary with Tuple Key:", coordinates)

# Accessing value using tuple key
print("✅ Coordinates:", coordinates[("lat", "lon")])


# 📌 14. Immutability Demonstration
immutable_tuple = (1, 2, 3)
print("\n🔒 Immutable Tuple:", immutable_tuple)

# Attempting to modify (will raise an error)
try:
    immutable_tuple[0] = 10  # ❌ TypeError: 'tuple' object does not support item assignment
except TypeError as e:
    print("❌ Error:", e)




# ------------------------Expected Output-------------------------------
🌟 Initial Tuple: ('🍎', '🍌', '🍊', '🍇')
✅ First fruit: 🍎
✅ Last fruit: 🍇

✂️ Original Tuple: (1, 2, 3, 4, 5)
➡️ First 3 elements: (1, 2, 3)
⬅️ Last 2 elements: (4, 5)

🚶‍♂️ Traversing the Tuple: 23, 45, tyson, 3.14, 

🧐 Is 🍎 in tuple? True
🧐 Is 🍉 in tuple? False

🔗 Combined Tuple: (1, 2, 3, 4, 5, 6)

🧮 Count of 1: 3
📍 Index of 4: 6

👤 Name: Alice
📅 Age: 30
🛠️ Profession: Engineer

✅ New Tuple After Adding 🍉: ('🍎', '🍌', '🍊', '🍇', '🍉')
❌ New Tuple After Removing 🍌: ('🍎', '🍊', '🍇')
🔄 New Tuple After Replacing 🍌 with 🍒: ('🍎', '🍒', '🍊', '🍇')

📦 Nested Tuple: (('🍎', '🍌'), ('🍊', '🍇'))
✅ First element of first tuple: 🍎
✅ Second element of second tuple: 🍇

🔄 List to Tuple: ('🍎', '🍌', '🍊', '🍇')
🔄 Tuple to List: ['🍎', '🍌', '🍊', '🍇']

🗺️ Dictionary with Tuple Key: {('lat', 'lon'): (37.7749, -122.4194)}
✅ Coordinates: (37.7749, -122.4194)

🔒 Immutable Tuple: (1, 2, 3)
❌ Error: 'tuple' object does not support item assignment
