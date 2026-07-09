def generateTable(n):
    # Create an empty string to store the multiplication table
    table = ""

    # Generate the table from 1 to 10
    for i in range(1, 11):

        # Append each line to the string
        table += f"{n} X {i} = {n*i}\n"

    # ---------------- Save the table to a file ----------------

    # Create a file named table_n.txt inside the 'tables' folder
    with open(f"tables/table_{n}.txt", "w") as f:

        # Write the complete table to the file
        f.write(table)


# Generate multiplication tables from 2 to 20
for i in range(2, 21):
    generateTable(i)


# ---------------------- NOTE ----------------------
# generateTable(n) creates the multiplication table of n.
#
# table += ... appends each multiplication line to the string.
#
# f"tables/table_{n}.txt"
# -> Creates dynamic filenames such as:
#    table_2.txt
#    table_3.txt
#    ...
#    table_20.txt
#
# "w" mode creates the file if it doesn't exist,
# otherwise it overwrites the existing file.
#
# The 'with' statement automatically closes the file
# after writing.
#
# The loop:
# for i in range(2, 21)
# generates and saves multiplication tables for
# numbers 2 through 20.
# --------------------------------------------------
