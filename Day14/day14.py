import random
import os
from art import logo, vs
from game_data import data

print(logo)
score = 0


def clear():
    return os.system("clear")


def compare(choice_a, choice_b):
    print(
        f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print(vs)
    print(
        f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

    answer = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    if answer == "a" and choice_a["follower_count"] > choice_b["follower_count"]:
        return choice_b
    elif answer == "b" and choice_b["follower_count"] > choice_a["follower_count"]:
        return choice_b
    else:
        return 0


compare_a = random.choice(data)
compare_b = random.choice(data)
if compare_a == compare_b:
    compare_b = random.choice(data)


compare_next = compare(compare_a, compare_b)

clear()
print(logo)

while compare_next != 0:
    score += 1
    print(f"You're right! Current score: {score}.")

    compare_a = compare_next
    while compare_a == compare_b:
        compare_b = random.choice(data)

    compare_next = compare(compare_a, compare_b)

print(f"Sorry, that's wrong. Final score: {score}")
