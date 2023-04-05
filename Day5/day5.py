# -----------------For Loop-------------------#
# For item in List:
#   Do something
# The loop allows us to execute the same line of code multiple times
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)

############### Exercise
# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

student_heights = input("Input a list of student heights: ")
heights_list = student_heights.split(" ")
total_height = 0

for height in heights_list:
    total_height += int(height)

average_height = total_height/len(heights_list)
print(average_height)