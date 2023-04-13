from art import logo, vs
import random
from game_data import data

# Compare function returns answer: Ask user which name has more followers between A and B. 
# If user chose A and followers A are higher than B return B else return 0
# If user chose B and followers B are higher than A return A right else wrong
def compare(choice_a, choice_b):
    answer = input(f"Who has more followers? Type 'A' or 'B': ")

    if answer == "A":
        if choice_a["follower_count"] > choice_b["follower_count"]:
            return choice_b
        else:
            return 0
    elif answer == "B":
        if choice_b["follower_count"] > choice_a["follower_count"]:
            return choice_a
        else:
            return 0

# Score function:  If answer not 0, clear screen, increase score by 1.
# Call compare function with A having answer from previous and B having new random
# else end game
def score()
        


# Print game logo from art.py file
print(logo)

# Find two ramdom indices from game_data file for comparison. Store them in A and B
compare_a = random.choice(data)
compare_b = random.choice(data)

print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
print(vs)
print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
