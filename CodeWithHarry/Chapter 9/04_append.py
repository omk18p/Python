st = "Hey Harry you are amazing"

# Open (or create) the file in append mode ('a')
# If the file exists, new data is added at the end.
# If it does not exist, a new file is created.
f = open("myfile.txt", "a")

# Append the string to the end of the file
f.write(st)

# Close the file to save the changes
f.close()

# ---------------------- NOTE ----------------------
# "a" (Append Mode)
# - Creates the file if it does not exist.
# - Adds new data to the end of the file.
# - Does NOT overwrite existing content.
# - write() appends the given string.
# - close() saves the changes and closes the file.
#
# Recommended approach:
#
# with open("myfile.txt", "a") as f:
#     f.write(st)
#
# The 'with' statement automatically closes the file.
# --------------------------------------------------
