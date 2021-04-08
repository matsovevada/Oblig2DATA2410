import library as lib
import random

class Test_bot:
    def __init__(self):
        self.name = "Test bot"
        self.id = None

    def register(self):
        response = lib.register_user(self.name)
        id = response['userID']
        bot.id = id
        print(f"User registered with name {self.name} and ID {id}")
        return id

    def create_room(self):
        room_names = ['Kollokvie', 'Just chatting', 'Seminar', 'Secret room', 'The room', 'The chat', 'TechChat', 'AllChat', 'TeamRoom', 'LocalChat']
       
        room_name = random.choice(room_names)
        
        # check that the room name isn't in use
        # rooms = lib.get_all_rooms(self.id)['rooms']
        rooms = lib.get_all_rooms(self.id)['rooms']

        for room in rooms:
            if room['name'] == room_name:
                room_name = f"{room_name} #{random.randint(1,10000)}"
                break
        
        lib.create_room(self.id, room_name)
        print(f"Room created with name {room_name}")

    def join_room(self):
        rooms = lib.get_all_rooms(self.id)['rooms']
        roomID = random.choice(list(rooms.keys()))
        room = lib.join_room(self.id, roomID)
        room_name = room['Room name']
        print(f"Joined room with name {room_name}")

    def main_function(self):
        # # Create user
        # print('Create user:')
        # response = lib.register_user(self.name)
        # self.id = response['userID']
        # print(response)

        # # Create room
        # print('Create room:')
        # room_name = "Rom"
        # print(lib.create_room(self.id, room_name))

        # # Join room
        # print('Join room:')
        # rooms = lib.get_all_rooms(self.id)['rooms']
        # roomID = random.choice(list(rooms.keys()))
        # print(lib.join_room(self.id, roomID))
       
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
bot.register()
print(bot.id)
print(lib.get_all_users(bot.id))
bot.create_room()
