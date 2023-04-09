# -----------------Functions with Outputs-------------------#
# They allow you to have an output once a function is completed
# def my_function():
#     return 3*2

# output = my_function()
# print(output)

def format_name(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()

    return f"{first_name} {last_name}"

formated_name = format_name("WaKABi", "brian")
print(formated_name)


    
