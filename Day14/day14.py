import random
import os
from art import logo, vs
from game_data import data


def clear():
    return os.system("clear")


def compare(choice_a, choice_b):
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print(vs)
    print( f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

    answer = input(f"Who has more followers? Type 'A' or 'B': ")

    if answer == "A" and choice_a["follower_count"] > choice_b["follower_count"]:
        return choice_b
    elif answer == "B" and choice_b["follower_count"] > choice_a["follower_count"]:
        return choice_a 
    else:
        return 0


def play_game():

    print(logo)
    score = 0

    compare_a = random.choice(data)
    compare_b = random.choice(data)

    compare_next = compare(compare_a, compare_b)

    while compare_next != 0:
        score += 1
        print(f"You're right! Current score: {score}.")

        compare_next = compare(compare_next, random.choice(data))
    print(f"Sorry, that's wrong. Final score: {score}")


play_game()
