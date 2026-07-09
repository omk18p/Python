print("a")          # Prints "a" and moves to the next line
print("b")          # Prints "b" and moves to the next line

# end="" prevents print() from moving to the next line
print("c", end="")  # Prints "c" without a newline

# Continues printing on the same line because of end=""
print("d", end="")  # Prints "d" without a newline

#Remember: By default, print() ends with \n (newline).
#end="" changes the ending, so the next print() continues on the same line.