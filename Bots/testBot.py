import library as lib
import random

class Test_bot:
    def __init__(self):
        self.name = "Test bot"
        self.id = None

    def main_function(self):
        # Create user
        print('Create user:')
        response = lib.register_user(self.name)
        self.id = response['userID']
        print(response)

        # Create room
        print('Create room:')
        room_name = "Rom"
        print(lib.create_room(self.id, room_name))

        # Join room
        print('Join room:')
        rooms = lib.get_all_rooms(self.id)['rooms']
        roomID = random.choice(list(rooms.keys()))
        print(lib.join_room(self.id, roomID))
       
        # Get user and user msg
        print('Get user and user msg:')
        room_users = lib.get_all_users_in_room(self.id, roomID)['Room users']
        random_user_in_room = random.choice(room_users)
        target_userID = random_user_in_room['userID'] 

        print(lib.get_messages_user(self.id, target_userID, roomID))


        # Send msg
        print('Send msg:')
        msg = "Hello"
        print(lib.send_message(self.id, roomID, msg))


        # Get room
        print('Get room:')
        rooms = lib.get_all_rooms(self.id)['rooms']
        roomID = random.choice(list(rooms.keys()))
        print(lib.get_room(self.id, roomID))

        # Get all users
        print('Get all users:')
        print(lib.get_all_users(self.id))

        # delete user
        print('Delete user:')
        print(lib.delete_user(1, self.id))

        # delete all users
        print('Delete all users:')
        print(lib.delete_all_users(self.id))

        # Get all users
        print('Get all users:')
        print(lib.get_all_users(self.id))


bot = Test_bot()
bot.main_function()
