class Employee:

    # Class attribute
    company = "ITC"

    # Instance method
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# Programmer inherits from Employee
class Programmer(Employee):

    # Overrides the parent class attribute
    company = "ITC Infotech"

    # Instance method specific to Programmer
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


# Create objects
a = Employee()
b = Programmer()

# Access class attributes
print(a.company, b.company)
# Output: ITC ITC Infotech


# ---------------------- NOTE ----------------------
# Inheritance:
# - Programmer inherits all accessible attributes and
#   methods from Employee.
#
# Class Attribute Overriding:
# - Employee.company = "ITC"
# - Programmer.company = "ITC Infotech"
#
# When:
# a.company
# Python uses Employee.company.
#
# When:
# b.company
# Python first checks Programmer, finds 'company',
# and uses "ITC Infotech".
#
# If Programmer did not define 'company',
# it would inherit Employee.company ("ITC").
#
# Output:
# ITC ITC Infotech
# --------------------------------------------------
