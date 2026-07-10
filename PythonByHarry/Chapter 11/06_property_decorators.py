
class Employee:

    # Class attribute
    a = 1

    # Class method
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    # Getter method
    # Allows 'name' to be accessed like an attribute.
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    # Setter method
    # Automatically called when assigning a value to 'name'.
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


# Create an object
e = Employee()

# Create an instance attribute
e.a = 45

# Calls the setter method
e.name = "Harry Khan"

# Print the first and last name
print(e.fname, e.lname)
# Output: Harry Khan

# Call the class method
e.show()
# Output: The class attribute of a is 1


# ---------------------- NOTE ----------------------
# @property:
# - Converts a method into a read-only attribute.
# - Allows access without parentheses.
#
# Example:
# e.name
# Internally calls:
# e.name()
#
# @name.setter:
# - Defines what happens when assigning a value
#   to the property.
#
# Example:
# e.name = "Harry Khan"
#
# Internally Python calls:
# e.name("Harry Khan")
#
# The setter splits the full name into:
# fname -> Harry
# lname -> Khan
#
# Advantages:
# - Encapsulation (hide internal implementation).
# - Validation can be added before storing values.
# - Existing code can keep using attributes while
#   the implementation changes internally.
#
# Difference:
# @property      -> Getter (read value)
# @property.setter -> Setter (update value)
# --------------------------------------------------
