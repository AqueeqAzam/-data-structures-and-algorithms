# 📌 1. Creating and Accessing Strings
# Definition: Strings are sequences of characters enclosed in quotes.
# Usage: Used in text processing, user input handling, and data storage.
greeting = "Hello, World!"
print("🌟 Initial String:", greeting)

# Access individual characters using indexing
print("\n🔍 Accessing Characters:")
print("✅ First character:", greeting[0])  # 🆗 Used in extracting initials
print("✅ Last character:", greeting[-1])  # 🔚 Used in checking file extensions


# 📌 2. Slicing Strings
# Definition: Slicing extracts a substring using a start and end index.
# Usage: Used in extracting file extensions, data manipulation, and NLP.
print("\n✂️ Slicing Strings:")
print("✅ First 5 characters:", greeting[:5])  # 🆕 Used in truncating names
print("✅ Last 6 characters:", greeting[-6:])  # 🔚 Used in retrieving file extensions
print("✅ Middle part (index 7 to 12):", greeting[7:12])  # 🎯 Extracting domain names


# 📌 3. Concatenating Strings
# Definition: Concatenation combines multiple strings using the + operator.
# Usage: Used in generating dynamic messages, creating usernames, and logging events.
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print("\n🔗 Concatenated String:", full_name)  # 🤝 Used in user profile creation


# 📌 4. String Formatting
# Definition: Formatting allows inserting variables into a string.
# Usage: Used in report generation, chatbots, and log messages.
age = 30
formatted_string = f"{first_name} {last_name} is {age} years old."
print("\n📝 Formatted String:", formatted_string)  # ✍️ Used in email templates

# Using .format() method
formatted_with_format = "{} {} is {} years old.".format(first_name, last_name, age)
print("📝 Formatted with .format():", formatted_with_format)  # ✍️ Used in system logs


# 📌 5. String Methods
# Definition: String methods perform operations like modifying or analyzing text.
# Usage: Used in data cleaning, search functions, and text transformation.
print("\n🛠️ String Methods:")
print("✅ Uppercase:", greeting.upper())  # 🔊 Used in headlines
print("✅ Lowercase:", greeting.lower())  # 🔉 Used in case-insensitive searches
print("✅ Title Case:", greeting.title())  # 🏷️ Used in formatting names
print("✅ Stripped of whitespace:", "   Hello   ".strip())  # ✂️ Used in cleaning user input
print("✅ Replaced 'World' with 'Python':", greeting.replace("World", "Python"))  # 🔄 Used in search and replace


# 📌 6. Searching and Membership
# Definition: These operations check for substrings in a string.
# Usage: Used in search engines, spam detection, and content filtering.
print("\n🧐 Searching and Membership:")
print("✅ Index of 'World':", greeting.index("World"))  # 📍 Used in text analysis
print("✅ Is 'Hello' in the string?", "Hello" in greeting)  # ❓ Used in keyword detection
print("✅ Starts with 'Hello'?", greeting.startswith("Hello"))  # 🏁 Used in checking file headers
print("✅ Ends with '!'?", greeting.endswith("!"))  # 🛑 Used in detecting exclamations


# 📌 7. Splitting and Joining
# Definition: Splitting breaks a string into words; joining merges them back.
# Usage: Used in CSV parsing, NLP tokenization, and log processing.
sentence = "Python is fun and powerful"
words = sentence.split()  # ✂️ Used in splitting sentences for NLP
print("\n✂️ Splitting String:", words)

joined_string = " ".join(words)  # 🤝 Used in reconstructing cleaned text
print("✅ Joined String:", joined_string)


# 📌 8. Iterating Over a String
# Definition: Iterating means processing each character in a loop.
# Usage: Used in spell checking, animations, and text-to-speech applications.
print("\n🚶‍♂️ Iterating Over the String:")
for char in greeting:
    print(char, end=", ")  # 👣 Used in typewriter text effects


# 📌 9. Checking String Properties
# Definition: These methods check if a string meets certain conditions.
# Usage: Used in form validation, password strength checks, and data verification.
print("\n📋 Checking String Properties:")
print("✅ Is alphanumeric?", "Hello123".isalnum())  # 🔢 Used in username validation
print("✅ Is alphabetic?", "Hello".isalpha())  # 🔤 Used in checking names
print("✅ Is numeric?", "123".isdigit())  # 🔢 Used in verifying numeric input


# 📌 10. Escaping Characters
# Definition: Escape sequences allow using special characters in strings.
# Usage: Used in generating HTML content and handling special characters.
escaped_string = "She said, \"Python is awesome!\""
print("\n🔒 Escaped String:", escaped_string)  # 🚪 Used in quotes within text


# 📌 11. Multiline Strings
# Definition: Strings spanning multiple lines using triple quotes.
# Usage: Used in storing multi-line content, comments, and documentation.
multiline_string = """This is a
multiline
string."""
print("\n📄 Multiline String:", multiline_string)  # 📜 Used in writing formatted articles


# 📌 12. Counting Substrings
# Definition: Counts occurrences of a substring in a string.
# Usage: Used in text analytics and frequency analysis.
print("\n🧮 Counting Substrings:")
print("✅ Number of 'l' in 'Hello, World!':", greeting.count("l"))  # 🔢 Used in word frequency


# 📌 13. Finding Substrings
# Definition: Returns the index of a substring or -1 if not found.
# Usage: Used in search engines and keyword analysis.
print("\n📍 Finding Substrings:")
print("✅ Find 'World':", greeting.find("World"))  # 🎯 Used in topic detection


# 📌 14. Reversing a String
# Definition: Reverse a string using slicing.
# Usage: Used in palindrome checking and encryption.
reversed_string = greeting[::-1]
print("\n🔄 Reversed String:", reversed_string)  # ↩️ Used in security hashing


# 📌 15. Length of a String
# Definition: The `len()` function returns the number of characters.
# Usage: Used in input validation and pagination.
print("\n📏 Length of the String:", len(greeting))  # 📏 Used in limiting text fields


# 📌 16. Converting Between Strings and Other Types
# Definition: Converts numbers to strings and vice versa.
# Usage: Used in databases, user input processing, and serialization.
number = 123
string_from_number = str(number)
print("\n🔄 Number to String:", string_from_number)  # 🔢➡️🔤 Used in ID handling


# 📌 17. Raw Strings
# Definition: Treats backslashes (\) as regular characters.
# Usage: Used in file paths and regex.
raw_string = r"C:\Users\Name\Documents"
print("\n📜 Raw String:", raw_string)  # 📂 Used in Windows file paths


# 📌 18. String Templates (Advanced Formatting)
# Definition: Templates allow placeholders for variable substitution.
# Usage: Used in email templates and dynamic web pages.
from string import Template
template = Template("Hello, $name!")
formatted_template = template.substitute(name="Alice")
print("\n📝 String Template:", formatted_template)  # 📋 Used in website personalization


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
