class Employee:

    # Class attributes
    # Shared by all objects of the Employee class
    language = "Python"
    salary = 1200000


# Create an object
harry = Employee()

# Creates an instance attribute named 'language'
# This shadows (overrides) the class attribute for this object only.
harry.language = "JavaScript"

# Prints the instance attribute 'language'
# and the class attribute 'salary'
print(harry.language, harry.salary)
# Output: JavaScript 1200000


# ---------------------- NOTE ----------------------
# Initially:
# Employee.language = "Python"
#
# After:
# harry.language = "JavaScript"
#
# Python creates a NEW instance attribute instead of
# modifying the class attribute.
#
# Attribute Lookup:
# 1. Look for an instance attribute.
# 2. If not found, use the class attribute.
#
# Therefore:
# harry.language        -> JavaScript (instance attribute)
# Employee.language     -> Python (class attribute)
#
# Other Employee objects will still have:
# language = "Python"
# --------------------------------------------------