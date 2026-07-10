class Employee:

    # Class attributes
    # Shared by all objects of the Employee class
    language = "Python"
    salary = 1200000

    # Instance method
    # 'self' refers to the object that calls this method.
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # Static method
    # Does not use 'self' or 'cls'.
    # Behaves like a normal function inside the class.
    @staticmethod
    def greet():
        print("Good morning")


# Create an object of Employee
harry = Employee()

# Call the static method
harry.greet()
# Output: Good morning

# Call the instance method
harry.getInfo()
# Output: The language is Python. The salary is 1200000

# Equivalent method call
# Employee.getInfo(harry)


# ---------------------- NOTE ----------------------
# Instance Method:
# - Takes 'self' as the first parameter.
# - Can access instance and class attributes.
# - Called using an object.
#
# Static Method:
# - Declared using @staticmethod.
# - Does not take 'self' or 'cls'.
# - Cannot directly access instance attributes.
# - Used for utility/helper functions related to the class.
#
# Method Calls:
# harry.getInfo()       -> Internally calls Employee.getInfo(harry)
# harry.greet()         -> Calls the static method directly.
#
# @staticmethod is used when a method belongs to the class
# but doesn't need information about any specific object.
# --------------------------------------------------
