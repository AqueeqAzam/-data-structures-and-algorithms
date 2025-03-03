# 📌 1. Creating and Accessing Strings
greeting = "Hello, World!"
print("🌟 Initial String:", greeting)

# Access individual characters
print("\n🔍 Accessing Characters:")
print("✅ First character:", greeting[0])  # 🆗
print("✅ Last character:", greeting[-1])  # 🔚


# 📌 2. Slicing Strings
print("\n✂️ Slicing Strings:")
print("✅ First 5 characters:", greeting[:5])  # 🆕
print("✅ Last 6 characters:", greeting[-6:])  # 🔚
print("✅ Middle part (from index 7 to 12):", greeting[7:12])  # 🎯


# 📌 3. Concatenating Strings
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print("\n🔗 Concatenated String:", full_name)  # 🤝


# 📌 4. String Formatting
age = 30
formatted_string = f"{first_name} {last_name} is {age} years old."
print("\n📝 Formatted String:", formatted_string)  # ✍️

# Using .format()
formatted_with_format = "{} {} is {} years old.".format(first_name, last_name, age)
print("📝 Formatted with .format():", formatted_with_format)  # ✍️


# 📌 5. String Methods
print("\n🛠️ String Methods:")
print("✅ Uppercase:", greeting.upper())  # 🔊
print("✅ Lowercase:", greeting.lower())  # 🔉
print("✅ Title Case:", greeting.title())  # 🏷️
print("✅ Stripped of whitespace:", "   Hello   ".strip())  # ✂️
print("✅ Replaced 'World' with 'Python':", greeting.replace("World", "Python"))  # 🔄


# 📌 6. Searching and Membership
print("\n🧐 Searching and Membership:")
print("✅ Index of 'World':", greeting.index("World"))  # 📍
print("✅ Is 'Hello' in the string?", "Hello" in greeting)  # ❓
print("✅ Starts with 'Hello'?", greeting.startswith("Hello"))  # 🏁
print("✅ Ends with '!'?", greeting.endswith("!"))  # 🛑


# 📌 7. Splitting and Joining
sentence = "Python is fun and powerful"
words = sentence.split()  # ✂️
print("\n✂️ Splitting String:", words)

joined_string = " ".join(words)  # 🤝
print("✅ Joined String:", joined_string)


# 📌 8. Iterating Over a String
print("\n🚶‍♂️ Iterating Over the String:")
for char in greeting:
    print(char, end=", ")  # 👣


# 📌 9. Checking String Properties
print("\n\n📋 Checking String Properties:")
print("✅ Is alphanumeric?", "Hello123".isalnum())  # 🔢
print("✅ Is alphabetic?", "Hello".isalpha())  # 🔤
print("✅ Is numeric?", "123".isdigit())  # 🔢
print("✅ Is lowercase?", "hello".islower())  # 🔡
print("✅ Is uppercase?", "HELLO".isupper())  # 🔠


# 📌 10. Escaping Characters
escaped_string = "She said, \"Python is awesome!\""
print("\n🔒 Escaped String:", escaped_string)  # 🚪


# 📌 11. Multiline Strings
multiline_string = """This is a
multiline
string."""
print("\n📄 Multiline String:", multiline_string)  # 📜


# 📌 12. Counting Substrings
print("\n🧮 Counting Substrings:")
print("✅ Number of 'l' in 'Hello, World!':", greeting.count("l"))  # 🔢


# 📌 13. Finding Substrings
print("\n📍 Finding Substrings:")
print("✅ Find 'World':", greeting.find("World"))  # 🎯
print("✅ Find 'Python':", greeting.find("Python"))  # ❌


# 📌 14. Reversing a String
reversed_string = greeting[::-1]
print("\n🔄 Reversed String:", reversed_string)  # ↩️


# 📌 15. Length of a String
print("\n📏 Length of the String:", len(greeting))  # 📏


# 📌 16. Converting Between Strings and Other Types
number = 123
string_from_number = str(number)
print("\n🔄 Number to String:", string_from_number)  # 🔢➡️🔤

list_of_chars = list(greeting)
print("🔄 String to List:", list_of_chars)  # 🔤➡️📦


# 📌 17. Raw Strings
raw_string = r"C:\Users\Name\Documents"
print("\n📜 Raw String:", raw_string)  # 📂


# 📌 18. String Templates (Advanced Formatting)
from string import Template
template = Template("Hello, $name!")
formatted_template = template.substitute(name="Alice")
print("\n📝 String Template:", formatted_template)  # 📋



#--------------------Expected Output-----------------------
🌟 Initial String: Hello, World!

🔍 Accessing Characters:
✅ First character: H 🆗
✅ Last character: ! 🔚

✂️ Slicing Strings:
✅ First 5 characters: Hello 🆕
✅ Last 6 characters: World! 🔚
✅ Middle part (from index 7 to 12): World 🎯

🔗 Concatenated String: Alice Smith 🤝

📝 Formatted String: Alice Smith is 30 years old. ✍️
📝 Formatted with .format(): Alice Smith is 30 years old. ✍️

🛠️ String Methods:
✅ Uppercase: HELLO, WORLD! 🔊
✅ Lowercase: hello, world! 🔉
✅ Title Case: Hello, World! 🏷️
✅ Stripped of whitespace: Hello ✂️
✅ Replaced 'World' with 'Python': Hello, Python! 🔄

🧐 Searching and Membership:
✅ Index of 'World': 7 📍
✅ Is 'Hello' in the string? True ❓
✅ Starts with 'Hello'? True 🏁
✅ Ends with '?' True 🛑

✂️ Splitting String: ['Python', 'is', 'fun', 'and', 'powerful']
✅ Joined String: Python is fun and powerful 🤝

🚶‍♂️ Iterating Over the String:
H, e, l, l, o, ,,  , W, o, r, l, d, !, 👣

📋 Checking String Properties:
✅ Is alphanumeric? True 🔢
✅ Is alphabetic? True 🔤
✅ Is numeric? True 🔢
✅ Is lowercase? True 🔡
✅ Is uppercase? True 🔠

🔒 Escaped String: She said, "Python is awesome!" 🚪

📄 Multiline String: This is a
multiline
string. 📜

🧮 Counting Substrings:
✅ Number of 'l' in 'Hello, World!': 3 🔢

📍 Finding Substrings:
✅ Find 'World': 7 🎯
✅ Find 'Python': -1 ❌

🔄 Reversed String: !dlroW ,olleH ↩️

📏 Length of the String: 13 📏

🔄 Number to String: 123 🔢➡️🔤
🔄 String to List: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!'] 🔤➡️📦

📜 Raw String: C:\Users\Name\Documents 📂

📝 String Template: Hello, Alice! 📋
