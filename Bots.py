import library as lib
import random


class Bots:
    def __init__(self, name):
        self.name = name
        self.id = None
        self.last_msgIDs = {}

    def register(self):
        response = lib.register_user(self.name)
        id = response['userID']
        self.id = id
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
    def send_message(self, msg):
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


class Per (Bots):
    def start(self):
        print('here')
        self.register()
        print('here2')
        self.join_room()
        print('here3')
        self.send_message('Skjera bagera?')
        print('here4')
