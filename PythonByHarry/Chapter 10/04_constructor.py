class Employee:

    # Class attributes
    language = "Python"
    salary = 1200000

    # Constructor (Dunder Method)
    # Automatically called when an object is created.
    def __init__(self, name, salary, language):
        self.name = name          # Instance attribute
        self.salary = salary      # Instance attribute
        self.language = language  # Instance attribute

        print("I am creating an object")

    # Instance method
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # Static method
    @staticmethod
    def greet():
        print("Good morning")


# Create an object
harry = Employee("Harry", 1300000, "JavaScript")

# Print instance attributes
print(harry.name, harry.salary, harry.language)
# Output:
# I am creating an object
# Harry 1300000 JavaScript

# rohan = Employee()


# ---------------------- NOTE ----------------------
# __init__():
# - A special (dunder) method called automatically
#   whenever an object is created.
# - Used to initialize instance attributes.
#
# Object Creation:
# Employee("Harry", 1300000, "JavaScript")
#
# Internally Python does:
# 1. Creates the object.
# 2. Calls:
#    __init__(harry, "Harry", 1300000, "JavaScript")
#
# Here:
# self      -> harry
# name      -> "Harry"
# salary    -> 1300000
# language  -> "JavaScript"
#
# The constructor initializes the object's data,
# so there is no need to assign attributes manually later.
# --------------------------------------------------
