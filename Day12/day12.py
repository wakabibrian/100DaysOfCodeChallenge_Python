# -----------------Namespaces: Local vs Global Scope-------------------#
# enemies = 1
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}") # 2

# increase_enemies()
# print(f"enemies outside function: {enemies}") # 1

# Local Scope: Exists within functions. Variables can only be used within the function they are defined
# def drink_portion():
#   portion_strength = 2
#   print(portion_strength)

# drink_portion()
# print(portion_strength) # Error

# Global Scope: Exists outside the function. Can be used anywhere within the file
# player_health = 10

# def drink_portion():
#     portion_strength = 2
#     print(portion_strength)
#     print(player_health)

# drink_portion()

# Global and Local Scope doesnt apply to only variables. It can also be applied to functions
# The above concept is known as the Namespace.
# Everything defined has a namespace and the namespace is valid in certain scopes

# -----------------Does Python have Blockscope?-------------------#
# There is no block  scope in Python
# game_level = 3
# enemies = ["skeleton", "zombie", "alien"]

# if game_level < 5:
#     new_enemies = enemies[0]

# print(new_enemies) # Valid

# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]

#     if game_level < 5:
#         new_enemies = enemies[0]

# print(new_enemies) # Invalid

# Scopes are only counted in functions

# -----------------How to modify variables with Global Scope-------------------#
# enemies = 1

# def increase_enemies():
#     global enemies
# #   enemies = 2 # This is a new variable, different from the global variable
#     enemies += 1 # Brings an error because you want to modify a variable which is not defined locally (to modify, use the global keyword)
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Always avoid modifying global variables, they are prune to errors

# Better way of using it, use the return concept.
# enemies = 1
# def increase_enemies():
#     return enemies + 1

# enemies = increase_enemies()
# print(enemies)

# -----------------Python constants and Global Scope-------------------#
# Global scopes can be useful especial when defining constants
# Global constants are variables defined and never planning on changing them
# PI = 3.143434 # Always use upper care by convension
# URL = "https:/google.com"
# TWITTER_HANDLE = "@wakabibrian"

# -----------------Day 12 Project: Number Guessing Game-------------------#
import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
game_ended = False


def guess_number():
    """Takes no inputs and returns a guessed number by the use"""
    print(f"You have {attempts} attempts remaining to guess the number")
    return int(input("Make a guess: "))


def result_message(message, attempts):
    """Takes message and attempts as inputs, prints message and returns attempts minus 1"""
    print(message)
    return attempts - 1


def level_turns():
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)
print(f"Pssst, the correct answer is {answer}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = level_turns()

while not game_ended:
    guess = guess_number()

    if attempts > 0:

        if guess > answer:
            attempts = result_message("Too high", attempts)
        elif guess < answer:
            attempts = result_message("Too low", attempts)
        else:
            print(f"You got it! The answer was {guess}.")
            game_ended = True

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        game_ended = True
