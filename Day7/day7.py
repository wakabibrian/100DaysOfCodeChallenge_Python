# -----------------Hangman Flow Chart-------------------#
# Break down a complex problem into a flow chart
# Flow chart saved in resources

# -----------------Challenge1: Picking a Random word and checking answers-------------------#
# -----------------Challenge2: Replacing Blanks with Guesses-------------------#
# -----------------Challenge3: Checking if the player has won-------------------#
# -----------------Challenge4: Keeping Track of player's lives-------------------#
# -----------------Challenge5: Importing modules and improving User Experience-------------------#

import random
import hangman_art
import hangman_words
import os

end_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
clear = lambda: os.system("clear")

logo = hangman_art.logo
print(logo)

# # Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display.append("_")

while not end_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You have already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

     
    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Loose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You win!")

    print(hangman_art.stages[lives])
