# -----------------Functions with Outputs-------------------#
# They allow you to have an output once a function is completed
# def my_function():
#     return 3*2

# output = my_function()
# print(output)

# def format_name(f_name, l_name):
#     first_name = f_name.title()
#     last_name = l_name.title()

#     return f"{first_name} {last_name}"

# formated_name = format_name("WaKABi", "brian")
# print(formated_name)

# -----------------Multiple return values-------------------#
# Return statement tells that its the end of the program hence exit
# Statements after the return statement will not be exexuted
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

formated_name = format_name(input("Enter first name: "), input("Enter first name: "))
print(formated_name)
