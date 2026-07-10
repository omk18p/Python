'''
a = "a very long string with emails"

emails = []
3 seconds
'''

# Open the file in read mode ('r')
f = open("file.txt", "r")

# Read the entire contents of the file
data = f.read()

# Print the file contents
print(data)

# Close the file to free system resources
f.close()

# ---------------------- NOTE ----------------------
# open("file.txt", "r") -> Opens the file in read mode.
# read()                -> Reads the entire file as a string.
# close()               -> Closes the file after use.
#
# It is recommended to use:
#
# with open("file.txt", "r") as f:
#     data = f.read()
#
# because the file is closed automatically, even if an error occurs.
# --------------------------------------------------

