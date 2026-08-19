
# Function of operator
def average(a, b):
    return (a+b)/2

def modules(a, b):
    return a%b


# Calling functions
f_num = float(input("Enter your first number: "))
s_num = float(input("Enter your second number: "))

operator = int(input("\nEnter 1 for Average \nEnter 2 for Modules \nSelect what you want to do:"))

if operator==1:
    print(f"Average to two numbers is {average(f_num,s_num)} ")

elif operator==2:
    print(f"Modules to two numbers is {modules(f_num,s_num)} ")
    
