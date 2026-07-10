class Demo:

    # Class attribute
    a = 4


# Create an object
o = Demo()

# Access the class attribute
# Since 'a' is not present in the object,
# Python looks for it in the class.
print(o.a)
# Output: 4

# Create an instance attribute 'a'
# This does NOT modify the class attribute.
o.a = 0

# Now Python finds 'a' in the object first,
# so it prints the instance attribute.
print(o.a)
# Output: 0

# Access the class attribute directly using the class name
print(Demo.a)
# Output: 4


# ---------------------- NOTE ----------------------
# Initially:
# Demo.a = 4 (Class attribute)
#
# When:
# o = Demo()
#
# The object 'o' has no attribute 'a'.
# So Python uses Demo.a.
#
# After:
# o.a = 0
#
# A new instance attribute 'a' is created for 'o'.
# It does NOT change Demo.a.
#
# Attribute Lookup Order:
# 1. Instance attributes
# 2. Class attributes
#
# Therefore:
# o.a      -> 0 (Instance attribute)
# Demo.a   -> 4 (Class attribute)
#
# Other Demo objects will still see:
# a = 4
# --------------------------------------------------
