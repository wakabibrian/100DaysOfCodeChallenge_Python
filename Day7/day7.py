
# -----------------Hangman Flow Chart-------------------#
# Break down a complex problem into a flow chart
# Flow chart saved in resources

# -----------------Challenge1: Picking a Random word and checking answers-------------------#
# -----------------Challenge2: Replacing Blanks with Guesses-------------------#
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display.append("_")

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    if chosen_word[position] == guess:
        display[position] = guess

print(display)
