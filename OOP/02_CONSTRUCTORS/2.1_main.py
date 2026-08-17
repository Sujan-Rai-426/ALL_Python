# Constructor is special method in class to create & initialize objects, AND assign its value 
# NOTE: Constructor syntax : def__init__(self):

class User():
    def __init__(self, username, level):
        self.username = username
        self.level = level
    
    def info(self):
        print(f" Level of {self.username} is {self.level} ")


user_1 = User("sujanrai426", 20)
user_1.info()

user_2 = User("playerunknown", 50)
user_2.info()

