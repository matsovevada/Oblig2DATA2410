import library as lib
import random
import time


class Bots:
    def __init__(self, name):
        self.name = name
        self.id = None
        self.last_msgIDs = {}
        self.QnA = None

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

        for roomID, room in rooms.items():
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


class Per(Bots):

    def start(self):
        self.create_room()
        self.join_room()
        time.sleep(6)
        self.send_message('Skjera bagera?')

class Quiz_master(Bots):
    
    def start(self):

        self.QnA = { 
            1 : "How many days does it take for the Earth to orbit the Sun?", 
            2 : "Until 1923, what was the Turkish city of Istanbul called?", 
            3 : "What’s the capital of Canada?",
            4 : "Name the longest river in the world",
            5 : "Where was the first modern Olympic Games held?",
            6 : "Which football team is known as ‘The Red Devils’?",
            7 : "What was the most-watched series on Netflix in 2019?",
            8 : "What is the capital of Norway?",
            9 : "What was the downloaded app in 2020?",
            10 : "What is the largest country in the world?",
            11 : "Which nationality was the polar explorer Roald Amundsen?",
            12 : "In bowling, what is the term given for three consecutive strikes?",
            13 : "Who was Donald Trump's vice president?",
            14 : "What was Britney Spears’ first single called?",
            15 : "What is David Bowie’s real name?"
        }
          
        # send a message to all rooms every 5th second
        while True:
            time.sleep(5)
            rooms = lib.get_all_rooms(self.id)['rooms']

            for roomID, room in rooms.items():
                if len(room['users']) > 0: # only send to rooms with users
                    question = random.choice(self.QnA)
                    lib.send_message(self.id, roomID, question)



        





