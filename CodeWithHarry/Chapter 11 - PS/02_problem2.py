class Animals:
    # Parent (Base) class
    pass


# Pets inherits from Animals
class Pets(Animals):
    pass


# Dog inherits from Pets
class Dog(Pets):

    # Static method
    @staticmethod
    def bark():
        print("Bow Bow!")


# Create an object of Dog
d = Dog()

# Call the static method
d.bark()
# Output: Bow Bow!


# ---------------------- NOTE ----------------------
# Multilevel Inheritance:
#
# Animals
#    ↑
# Pets
#    ↑
# Dog
#
# - Pets inherits from Animals.
# - Dog inherits from Pets.
# - Therefore, Dog indirectly inherits from Animals.
#
# A child class inherits all accessible members
# of its parent classes.
#
# @staticmethod:
# - Does not require 'self' or 'cls'.
# - Can be called using an object or the class name.
#
# Example:
# d.bark()
# Dog.bark()
#
# Both produce:
# Bow Bow!
# --------------------------------------------------

