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

# student_heights = input("Input a list of student heights: ")
# heights_list = student_heights.split(" ")
# total_height = 0

# for height in heights_list:
#     total_height += int(height)

# average_height = total_height/len(heights_list)
# print(average_height)

#### Option 2
# student_heights = input("Input a list of student heights. ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# total_height = 0
# total_students = 0

# for height in student_heights:
#     total_height += height
#     total_students += 1

# average_height = round(total_height/total_students)
# print(average_height)

###### Exercise 2
# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Dont use max() function

# scores_list = input("Input a list of student scores ").split(" ")
# for n in range(0, len(scores_list)):
#     scores_list[n] = int(scores_list[n])

# highest_score = 0

# for score in scores_list:
#     if score > highest_score:
#         highest_score = score

# print(f"The highest score in the class is {highest_score}")

# -----------------For loops and the range() function-------------------#
# Sometimes we may want to work on something which is not a list
# for number in range(a, b): # Holds a number between a and b and not including b
#   print(number)

# for number in range(1, 11, 3): # 3 specifies how the step will be
#     print(number)

#### Exercise: 
# Adding all the numbers between 1 and 100
# sum = 0
# for number in range (1, 101):
#     sum += number

# print(sum)

#### Exercise:
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100:
# sum = 0
# for number in range(2, 101, 2):
#     sum += number
# print(sum)

####### Exercise 
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
#   Your program should print each number from 1 to 100 in turn.
#   When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#   When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)