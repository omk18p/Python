def rem(l, word):
    n = []

    for item in l:
        if not (item == word):
            n.append(item.strip(word))

    return n


l = ["Harry", "Rohan", "Shubham", "an"]

print(rem(l, "an"))

# ---------------------- NOTE ----------------------
# strip(chars) does NOT remove the given word.
# It removes ALL characters present in 'chars'
# only from the beginning and end of the string.
#
# Examples:
# "Rohan".strip("an")  -> "Roh"
# "an".strip("an")     -> ""
# "banana".strip("an") -> "b"
#
# If you want to remove a word from anywhere in a string,
# use replace() instead.
#
# Example:
# "Rohan".replace("an", "") -> "Roh"
# --------------------------------------------------