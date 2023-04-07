
# -----------------Hangman Flow Chart-------------------#
# Break down a complex problem into a flow chart
# Flow chart saved in resources

# -----------------Challenge1: Picking a Random word and checking answers-------------------#
# -----------------Challenge2: Replacing Blanks with Guesses-------------------#
# -----------------Challenge3: Checking if the player has won-------------------#
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display.append("_")

# TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word 
# and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    print(display)

print("You win!")
