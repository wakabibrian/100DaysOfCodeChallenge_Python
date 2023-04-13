from art import logo, vs
import random
from game_data import data


# Print game logo from art.py file
print(logo)

# Find two ramdom indices from game_data file for comparison. Store them in A and B
compare_a = random.choice(data)
compare_b = random.choice(data)
print(compare_a["name"])
print(compare_b["name"])

# Compare function returns answer: Ask user which name has more followers between A and B. 
# If user chose A and followers A are higher than B return B else return 0
# If user chose B and followers B are higher than A return A right else wrong

# Score function:  If answer not 0, clear screen, increase score by 1.
# Call compare function with A having answer from previous and B having new random
# else end game