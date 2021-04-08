import library as lib
import random

class Test_bot:
    def __init__(self):
        self.name = "Test bot"
        self.id = None
        self.last_msgIDs = {}

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

    def bot_message(self):
        return "Halloi"


    
    # Iterates over all chatrooms and finds rooms where the bot is present, returns list of roomID(s)
    def bot_in_rooms(self):
        bot_in_rooms_list = []
        rooms = lib.get_all_rooms(self.id)['rooms']
        for roomID, room in rooms.items():
                for user in room['users']:
                    if user['userID'] == self.id:
                        bot_in_rooms_list.append(roomID)
        return bot_in_rooms_list

    # Send message to random room where the bot is present
    def send_message(self):
        msg = self.bot_message()
        roomID_list = self.bot_in_rooms()
        target_roomID = random.choice(roomID_list)
        lib.send_message(self.id, target_roomID, msg)

    # Get messages in room, last_msgID makes sure only new messages are printed to the client  
    def get_messages_in_room(self, roomID):
        messages = lib.get_messages_in_room(self.id, roomID)['All messages:']

        if roomID in self.last_msgIDs:
            counter = self.last_msgIDs[roomID]
            for message in messages:
                if counter < message['msgID']:
                    userID = message['userID']
                    msg = message['msg_content']
                    print(f"Room: {roomID} , {userID}: {msg}")
                    counter = counter+1
            
            self.last_msgIDs[roomID] = counter

        else:
            for message in messages:
                userID = message['userID']
                msg = message['msg_content']
                print(f"Room: {roomID} , {userID}: {msg}")

            self.last_msgIDs[roomID] = len(messages)
            

                    


        


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
        #print('Send msg:')
        #msg = "Hello"
        #print(lib.send_message(self.id, roomID, msg))


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
#print(bot.id)
#print(lib.get_all_users(bot.id))
#bot.create_room()
#bot.join_room()
#bot.send_message()

lib.join_room(bot.id, 1)
bot.get_messages_in_room(1)
lib.send_message(bot.id, 1, "Halloi")
lib.send_message(bot.id, 1, "halloi")
bot.get_messages_in_room(1)
lib.send_message(bot.id, 1, "siste")
bot.get_messages_in_room(1)


