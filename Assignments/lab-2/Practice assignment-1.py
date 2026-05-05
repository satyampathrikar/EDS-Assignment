# Creating a list
lst = [10, 20, 30, 40]

# Append
lst.append(50)

# Insert
lst.insert(1, 15)

# Remove
lst.remove(30)

# Pop
lst.pop()

# Reverse
lst.reverse()

# Sort
lst.sort()

print("Final List:", lst)

# Creating dictionary
student = {"name": "John", "age": 20}

# Add item
student["marks"] = 85

# Update
student["age"] = 21

# Remove
student.pop("age")

# Keys, Values, Items
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())