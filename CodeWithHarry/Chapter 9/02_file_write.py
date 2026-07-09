st = "Hey Harry you are amazing"

# Open (or create) the file in write mode ('w')
# If the file already exists, its contents will be overwritten.
f = open("myfile.txt", "w")

# Write the string to the file
f.write(st)

# Close the file to save the changes and free resources
f.close()

# ---------------------- NOTE ----------------------
# "w" (Write Mode)
# - Creates the file if it does not exist.
# - Overwrites the file if it already exists.
# - write() writes the given string to the file.
# - close() ensures the data is saved and the file is closed.
#
# Recommended approach:
#
# with open("myfile.txt", "w") as f:
#     f.write(st)
#
# The 'with' statement automatically closes the file.
# --------------------------------------------------
