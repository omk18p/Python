s = set()

# Adds integer 20 to the set
s.add(20)

# 20.0 is considered equal to 20 in Python
# because 20 == 20.0 is True, so it is NOT added again.
s.add(20.0)

# '20' is a string, so it is different from the integer 20
# and is added to the set.
s.add('20')

# Prints the number of unique elements in the set
print(len(s))
# Output: 2