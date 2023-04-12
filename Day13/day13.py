# Debugging - The process of removing bugs from your code
###########Tips and techniques of finding bugs and removing them

# -----------------Describe a problem-------------------#
# def my_function():
# #   for i in range(1, 20):
#   for i in range(1, 21): # Correct
#     if i == 20:
#       print("You got it")
# my_function()
# The for loop is supposed to print when i reaches with an assumption of 20, but actually range doesnt reach 20

# -----------------Reproduce the Bug-------------------#
from random import randint
dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])