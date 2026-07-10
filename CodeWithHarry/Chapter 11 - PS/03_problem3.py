
class Employee:

    # Class attributes
    salary = 234
    increment = 20

    # Getter property
    # Calculates salary after applying the increment.
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment / 100))

    # Setter property
    # Updates the increment based on the desired salary.
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100


# Create an object
e = Employee()

# print(e.salaryAfterIncrement)
# Output: 280.8

# Calls the setter to calculate the required increment
e.salaryAfterIncrement = 280.8

# Print the updated increment
print(e.increment)
# Output: 20.0


# ---------------------- NOTE ----------------------
# @property:
# - Creates a computed (derived) attribute.
# - salaryAfterIncrement is calculated dynamically
#   from salary and increment.
#
# Formula:
# salaryAfterIncrement =
# salary + (salary × increment / 100)
#
# @salaryAfterIncrement.setter:
# - Allows assigning a value to salaryAfterIncrement.
# - Instead of changing salary, it calculates and
#   updates the required increment.
#
# Formula:
# increment = ((new_salary / salary) - 1) × 100
#
# Here:
# salary = 234
# new salary = 280.8
#
# increment = ((280.8 / 234) - 1) × 100
#           = 20%
#
# Advantages:
# - Encapsulation of calculation logic.
# - Users work with salaryAfterIncrement like a
#   normal attribute.
# - Getter computes the value.
# - Setter updates the dependent attribute.
# --------------------------------------------------
