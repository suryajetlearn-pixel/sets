# Create two sets
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}

# Union
print("Union:", a | b)

# Intersection
print("Intersection:", a & b)

# Difference
print("A - B:", a - b)
print("B - A:", b - a)

# Symmetric Difference
print("Symmetric Difference:", a ^ b)   

# Convert a list into a set
sample_list = [1, 1, 2, 2, 3, 3]
sample_set = set(sample_list)
print("Set from list:", sample_set)

# Check if an element exists
if 4 in sample_set:
    print("4 is present")
else:
    print("4 is not present")

# Add elements
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(3)

print("After adding:", myset)

# Remove elements
myset.remove(2)
print("After removing 2:", myset)

# Discard an element
myset.discard(5)
print("Final set:", myset)