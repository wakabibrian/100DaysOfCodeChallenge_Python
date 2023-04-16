# -----------------How to create own classes-------------------#
# Remember - A class is a blue print for creating an object
# Syntax
# class User: 
#     pass
# # The name of the class should have the first name of each letter capitalised (PascalCase)
# # PascalCase - classes, snake_case for other things

# user_1 = User()

# -----------------Working with Attributes, Class Constructors and the __init__() Functions-------------------#
# -----------------Adding Methods to a Class-------------------#
# Creating attributes from objects: not a good way
# An attribute is a variable associated with an object
# user_1.id = "0001"
# user_1.name = "Wakabi"
# print(user_1.name)

# Creating attributes using a connstructor: Better way
# Constructor specifies what should happen when the object is created: initializing an object 
# When an object is created, we can set variables to their starting values
# In python, to create a constructor we use the __init__ function
# __init__ function is used to initialise the attributes
# class Car:
#     def __init__(self):
#         pass
#         #initialise attributes

# When a  function  is attached to an object is called a method

# class User:
#     def __init__(self, user_id, username):
#         # Remember attributes are the things that the object will have (variables associated with the final object)
#         # self represents the object that was created from a particular class (its a convention, you can use any word.)
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
    
#     def follow(self, user):
#         # A method should always have a self parameter as the first parameter: whenever it is called, it knows the object that called it.
#         user.followers += 1
#         self.following += 1
#         #object.attribute
        


# # The __init__ fununction will always be called everytime you will create a new objects
# user_1 = User("0001", "Wakabi")
# user_2 = User("0002", "Britney")
# print(user_1.username)
# print(user_2.id)
# print(user_1.followers)

# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)

# -----------------Day 17 Project: Quiz-------------------#


