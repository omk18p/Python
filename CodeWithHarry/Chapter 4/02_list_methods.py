friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

# Prints the original list
print(friends)
# Output: ['Apple', 'Orange', 5, 345.06, False, 'Aakash', 'Rohan']

# Adds "Harry" at the end of the list
friends.append("Harry")

# Prints the updated list
print(friends)
# Output: ['Apple', 'Orange', 5, 345.06, False, 'Aakash', 'Rohan', 'Harry']


l1 = [1, 34, 62, 2, 6, 11]

# Sorts the list in ascending order
# l1.sort()
# Output: [1, 2, 6, 11, 34, 62]

# Reverses the list
# l1.reverse()
# Output: [11, 6, 2, 62, 34, 1]

# Inserts 333333 at index 2
# l1.insert(2, 333333)
# Output: [1, 34, 333333, 62, 2, 6, 11]

# Removes and returns the element at index 3
value = l1.pop(3)

# Prints the removed element
print(value)
# Output: 2

# Prints the updated list
print(l1)
# Output: [1, 34, 62, 6, 11]