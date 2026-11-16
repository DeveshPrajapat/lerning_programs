# A tuple is an ordered, immutable collection of elements in Python.

# Ordered → The elements maintain the sequence in which they were defined.

# Immutable → Once created, you cannot change (add, remove, or update) the elements of a tuple.

# Can store heterogeneous data types (integers, strings, lists, etc.).

# Defined using parentheses () or without any brackets in some cases.

#! Syntax
# tuple_name = (element1, element2, element3, ...)

#?Example
# Creating a tuple
student = ("Amit", 21, "CSE")

print(student)         # Output: ('Amit', 21, 'CSE')
print(student[0])      # Output: Amit (accessing first element)
print(student[-1])     # Output: CSE (accessing last element)

# Tuple can contain different data types
mixed_tuple = (10, "Hello", 3.14, [1, 2, 3])

# Nested tuple
nested = (1, (2, 3), (4, 5))

# Length of tuple
print(len(student))    # Output: 3