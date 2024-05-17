# Create a dictionary of student information
student = {
    "name": "Teoh",
    "age": int(20),
    "major": "Decision Science",
    "grades": {
        "math": 95,
        "english": 80,
        "history": 85
    }
}

# Access dictionary values by keys
student_name = student["name"]
student_age = student["age"]

# Modify dictionary values
student["age"] = 22
student["grades"]["math"] = 97

# Add a new key-value pair
student["gender"] = "Male"

# Check if a key exists in the dictionary
has_major = "major" in student
has_height = "height" in student

# Get the list of keys and values
keys = student.keys()
values = student.values()

# Iterate through the dictionary
print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")

# Remove a key-value pair
del student["grades"]

# Print the updated dictionary
print("\nStudent Information after removing 'grades':")
for key, value in student.items():
    print(f"{key}: {value}")

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my