# NOTE: Class is parent and objects are its childrens

class User:
    username = "sujanrai426"
    email = "rsujan140@gmail.com"
    mobile = "987654321"
    player_id = "SP100RS2QZ11"
    level = 1

    def info (self):
        print(f" Player details :-\n username = {self.username}\n email = {self.email}\n mobile = {self.mobile}\n player_id = {self.player_id}\n level = {self.level}\n ")


user_1 = User() 
user_1.email = "sujanrai@gmail.com"
user_1.level = 15
user_1.info()

user_2 = User()
user_2.level = 10
user_2.info()