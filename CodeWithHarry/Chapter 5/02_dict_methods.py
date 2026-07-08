marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

# Returns all key-value pairs as dict_items
# print(marks.items())
# Output: dict_items([('Harry', 100), ('Shubham', 56), ('Rohan', 23), (0, 'Harry')])

# Returns all keys
# print(marks.keys())
# Output: dict_keys(['Harry', 'Shubham', 'Rohan', 0])

# Returns all values
# print(marks.values())
# Output: dict_values([100, 56, 23, 'Harry'])

# Updates an existing key ("Harry") and adds a new key ("Renuka")
# marks.update({"Harry": 99, "Renuka": 100})
# print(marks)
# Output: {'Harry': 99, 'Shubham': 56, 'Rohan': 23, 0: 'Harry', 'Renuka': 100}

# get() returns None if the key does not exist
print(marks.get("Harry2"))
# Output: None

# Accessing a missing key using [] raises a KeyError
# print(marks["Harry2"])
# Output: KeyError: 'Harry2'