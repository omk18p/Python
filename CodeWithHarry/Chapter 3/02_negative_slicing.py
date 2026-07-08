name = "Harry"

# Slicing from index 0 to 2 (3 is excluded)
print(name[0:3])      # Har

# Negative indexing: starts from -4 ('a') to -2 ('r'), -1 is excluded
print(name[-4:-1])    # arr

# Slicing from index 1 to 3 (4 is excluded)
print(name[1:4])      # arr

# Start index omitted → starts from 0
print(name[:4])       # Harr
# Same as: print(name[0:4])

# End index omitted → goes till the end of the string
print(name[1:])       # arry
# Same as: print(name[1:5])

# Slicing from index 1 to 4 (5 is excluded)
print(name[1:5])      # arry