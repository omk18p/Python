import random  # Import the random module

def game():
    # Display a message when the game starts
    print("You are playing the game..")

    # Generate a random score between 1 and 62
    score = random.randint(1, 62)

    # ---------------- Read the current high score ----------------
    with open("hiscore.txt") as f:
        hiscore = f.read()

        # Check if the file is not empty
        if(hiscore != ""):
            hiscore = int(hiscore)   # Convert high score from string to integer
        else:
            hiscore = 0              # If file is empty, initialize high score to 0

    # Display the current score
    print(f"Your score: {score}")

    # ---------------- Update high score if needed ----------------
    if(score > hiscore):

        # Open the file in write mode and save the new high score
        with open("hiscore.txt", "w") as f:
            f.write(str(score))      # Convert integer to string before writing

    # Return the generated score
    return score


# Start the game
game()


# ---------------------- NOTE ----------------------
# random.randint(1, 62) -> Generates a random integer between 1 and 62.
#
# read() always returns a string, so int() is used to convert
# the high score into an integer for comparison.
#
# write() accepts only strings, so str(score) is used before writing.
#
# "w" mode overwrites the previous high score with the new one.
#
# The high score is updated only if:
#     score > hiscore
#
# If hiscore.txt is empty, the high score is initialized to 0.
#
# The 'with' statement automatically closes the file after use.
# --------------------------------------------------

