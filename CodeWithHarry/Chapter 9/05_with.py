# Open the file in read mode (default mode is 'r')
f = open("file.txt")

# Read and print the entire file content
print(f.read())

# Close the file manually
f.close()


# ---------------- Using 'with' Statement ----------------

# Open the file using the 'with' statement
# The file is automatically closed after this block.
with open("file.txt") as f:

    # Read and print the entire file content
    print(f.read())


# ---------------------- NOTE ----------------------
# open()          -> Opens a file.
# read()          -> Reads the entire file as a string.
# close()         -> Closes the file manually.
#
# with open() as f:
# - Automatically closes the file after use.
# - Safer and recommended, even if an exception occurs.
# - No need to call close() explicitly.
# --------------------------------------------------
