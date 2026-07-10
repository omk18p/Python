class Employee:

    # Class attributes
    # Shared by all objects of the Employee class
    language = "Py"
    salary = 1200000


# Create the first object
harry = Employee()

# Instance attribute (belongs only to harry)
harry.name = "Harry"

# Access instance and class attributes
print(harry.name, harry.language, harry.salary)
# Output: Harry Py 1200000


# Create the second object
rohan = Employee()

# Instance attribute (belongs only to rohan)
rohan.name = "Rohan Roro Robinson"

# Access instance and class attributes
print(rohan.name, rohan.salary, rohan.language)
# Output: Rohan Roro Robinson 1200000 Py


# ---------------------- NOTE ----------------------
# Class Attributes:
# - Declared inside the class but outside methods.
# - Shared by all objects of the class.
# - Example: language, salary
#
# Instance Attributes:
# - Created for a specific object.
# - Each object has its own copy.
# - Example: name
#
# Attribute Lookup Order:
# 1. Python first looks for an instance attribute.
# 2. If not found, it looks for a class attribute.
#
# Here:
# harry.name and rohan.name -> Instance attributes
# language and salary       -> Class attributes
# --------------------------------------------------
