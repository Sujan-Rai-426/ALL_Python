# NOTE: Take list as input from user and print the list
# NOTE: Also we use For loop and split and strip method

raw_input = input("Enter your list elements separated by comma (,) : ")

user_list = [item.strip() for item in raw_input.split(',')]

print("\nYour list is : ", user_list)