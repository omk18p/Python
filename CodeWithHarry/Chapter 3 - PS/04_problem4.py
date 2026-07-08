name = "Harry is a good  boy and  "

# replace(old, new) returns a NEW string with all occurrences
# of 'old' replaced by 'new'.
print(name.replace("  ", " "))   # Harry is a good boy and 

# The original string remains unchanged because
# strings in Python are immutable.
print(name)                      # Harry is a good  boy and  