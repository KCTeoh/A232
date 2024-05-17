# Create a list of numbers
numbers = [6, 7, 8, 9, 10]

# Print the list
print("Original list:", numbers)

# Access elements by index
first_element = numbers[0]
print("The first element is:", first_element)


# Slice the list to get a subset
subset = numbers[2:4]
print("Subset of the list:", subset)

# Modify an element in the list
numbers[1] = 2
print("Modified list:", numbers)



# Append an element to the end of the list
numbers.append(11)
print("List after appending 11:", numbers)

# Remove an element by value
numbers.remove(6)
print("List after removing 6:", numbers)


# Find the index of an element
index_of_9 = numbers.index(9)
print("Index of 9:", index_of_9)

# Check if an element is in the list
contains_10 = 10 in numbers
print("Does the list contain 10?", contains_10)


# Sort the list
numbers.sort()
print("Sorted list:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)

 
# Create a list of strings
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my