words = ["Donkey", "bad", "ganda"]  # List of words to be censored

# ---------------- Read the file ----------------
with open("file.txt", "r") as f:

    # Read the entire file content as a string
    content = f.read()

# ---------------- Replace banned words ----------------
for word in words:

    # Replace each banned word with '*' characters
    # len(word) ensures the number of '*' matches the word length
    content = content.replace(word, "#" * len(word))

# ---------------- Write the updated content ----------------
with open("file.txt", "w") as f:

    # Save the censored content back to the file
    f.write(content)


# ---------------------- NOTE ----------------------
# read() -> Reads the entire file into a string.
#
# replace(old, new) -> Replaces all occurrences of 'old'
# with 'new' and returns a new string.
#
# "#" * len(word)
# -> Creates a string of '#' having the same length
# as the banned word.
#
# Examples:
# "bad"    -> ###
# "Donkey" -> ######
# "ganda"  -> #####
#
# The loop replaces every banned word in the file.
#
# Finally, the updated content is written back to
# the same file using write mode ('w').
# --------------------------------------------------
