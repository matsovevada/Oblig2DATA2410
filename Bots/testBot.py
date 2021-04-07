import library as lib
import random

class Test_bot:
    def __init__(self):
        self.name = "Test bot"
        self.id = None

    def main_function(self):
        response = lib.register_user(self.name)
        self.id = response['userID']
        # rooms = {0: {'name': "testerinoroom", 'users': [{'username' : "Test" , 'userID' : 4}], 'messages': []}}
        rooms = lib.get_all_rooms(self.id)['rooms']
        roomID = random.choice(list(rooms.keys()))
        print(lib.join_room(self.id, roomID))
        print(self.id)

bot = Test_bot()
bot.main_function()