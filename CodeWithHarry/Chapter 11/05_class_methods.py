class Employee:

    # Class attribute
    a = 1

    # Class method
    # 'cls' refers to the class itself, not an object.
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


# Create an object
e = Employee()

# Create an instance attribute
e.a = 45

# Call the class method
e.show()
# Output: The class attribute of a is 1


# ---------------------- NOTE ----------------------
# @classmethod:
# - Takes 'cls' (class) as the first parameter.
# - Works with class attributes.
# - Can modify class attributes.
#
# Here:
# Employee.a = 1
#
# After:
# e.a = 45
#
# An instance attribute 'a' is created for object 'e'.
# It does NOT change Employee.a.
#
# Inside show():
# cls.a refers to Employee.a, not e.a.
#
# Therefore:
# e.a          -> 45 (Instance attribute)
# Employee.a   -> 1  (Class attribute)
# cls.a        -> 1
#
# Difference:
# - self  -> Refers to the current object (instance).
# - cls   -> Refers to the class itself.
# --------------------------------------------------