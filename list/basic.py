
# A list in Python is an ordered, mutable collection of elements.

# Ordered → The elements keep the order in which they were added.

# Mutable → You can add, remove, or change elements after the list is created.

# Can store heterogeneous data types (integers, strings, floats, objects, etc.).

# Defined using square brackets [].

# Syntax
# list_name = [element1, element2, element3, ...]

# Example
# Creating a list
fruits = ["apple", "banana", "cherry"]

print(fruits)         # Output: ['apple', 'banana', 'cherry']
print(fruits[0])      # Output: apple
print(fruits[-1])     # Output: cherry

# Adding elements
fruits.append("mango")   # Adds to end
fruits.insert(1, "kiwi") # Adds at specific position

# Removing elements
fruits.remove("banana")  # Remove by value
fruits.pop(0)            # Remove by index

# Updating elements
fruits[0] = "grapes"     # Modify value

# Length of list
print(len(fruits))       # Output depends on current list size

# Nested list
nested = [1, [2, 3], [4, 5]]

# Iterating over a list
for item in fruits:
    print(item)

# Key Points

# Mutable → Changes reflect directly in the same list object.

# Allows duplicates.

# Supports slicing (fruits[1:3]).

# Common methods: append(), extend(), insert(), remove(), pop(), sort(), reverse().


li = ["StringS","Boys","Devesh",'1221']
c = 0

for i in range(0,len(li)):
    print(f"Number of items in list is {len(li)}\nIndex number is {i}\nItems in list is {li[i]}\n===============================================")
for i in li:
    print(f"Items inner index number {i[0]}, {i[-1]}\n=====================================")