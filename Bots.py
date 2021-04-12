import library as lib
import random
import time

## BOTS ##


# Super-class for making bots
class Bots:
    def __init__(self, name):
        self.name = name
        self.id = None
        self.last_msgIDs = {}
        self.QnA = None
        self.bot_sleep = None

    # Makes the bot register itself in the program
    def register(self):
        response = lib.register_user(self.name)
        regid = response['userID']
        self.id = id
        print(f"User registered with name {self.name} and ID {regid}")
        return id

    # Makes the bot create a chat-room on the server
    def create_room(self):
        room_names = ['Kollokvie', 'JustChatting', 'Seminar', 'SecretRoom', 'TheRoom', 'TheChat', 'TechChat', 'AllChat',
                      'TeamRoom', 'LocalChat']
       
        room_name = random.choice(room_names)
        
        # check that the room name isn't in use
        # rooms = lib.get_all_rooms(self.id)['rooms']
        rooms = lib.get_all_rooms(self.id)['rooms']

        for roomID, room in rooms.items():
            if room['name'] == room_name:
                room_name = f"{room_name}#{random.randint(1,10000)}"
                break
        
        lib.create_room(self.id, room_name)
        print(f"{self.name} created room {room_name}")

    # Makes the bot join a chat-room
    def join_room(self):
        rooms = lib.get_all_rooms(self.id)['rooms']

        roomID = random.choice(list(rooms.keys()))
        break_counter = 0
        while roomID in self.bot_in_rooms():
            if break_counter > 20:    # abort if a suitable room is not found in 20 tries
                return

            roomID = random.choice(list(rooms.keys()))
            break_counter = break_counter + 1

        room = lib.join_room(self.id, roomID)
        room_name = room.get('Room name')
        print(f"Joined room with name {room_name}")
        # update last_msgIDs
        messages_in_room = lib.get_messages_in_room(self.id, roomID)['All messages:']
        if messages_in_room:
            self.last_msgIDs[roomID] = messages_in_room[-1]['msgID']  

    # Returns a list of all rooms where bots have joined
    def get_all_rooms(self):
        return self.bot_in_rooms()

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
    def send_message(self, msg, roomID):
        # sleep-interval different for each bot
        time.sleep(self.bot_sleep)
        lib.send_message(self.id, roomID, msg)
        msg_formatted = "[" + lib.get_room(self.id, roomID)['room']['name'] + "] Me: " + msg
        print(msg_formatted)

    # Get messages in room, last_msgID makes sure only new messages are printed to the client  
    def get_messages_in_room(self, roomID, sender_userID=None):

        messages = lib.get_messages_in_room(self.id, roomID)['All messages:']
        room_name = lib.get_room(self.id, roomID)['room']['name']

        if messages:
            # checks if the bot has unread messages in the room
            if self.last_msgIDs.get(roomID) != messages[len(messages)-1]['msgID']:

                unread_messages = []

                if self.last_msgIDs.get(roomID) is None:
                    counter = messages[len(messages) - 1]['msgID']
                else:
                    counter = self.last_msgIDs[roomID]

                for message in messages:
                    if counter <= message['msgID']:
                        userID = message['userID']
                        msg_content = message['msg_content']
                        username = lib.get_specific_user(userID, self.id)['user']['name']
                        msg = f"[{room_name}] {username}: " + msg_content
                            
                        counter = counter+1
                        # if sender_userID is supplied, don't include messages from the bot itself
                        if sender_userID:
                            if userID != sender_userID:
                                unread_messages.append(msg)
                        else:
                            unread_messages.append(msg)

                self.last_msgIDs[roomID] = counter
                return unread_messages

        else:
            return None
       

class Quiz_master(Bots):
    
    def start(self):

        self.bot_sleep = 20

        self.QnA = { 
            1: "How many days does it take for the Earth to orbit the Sun?",
            2: "Until 1923, what was the Turkish city of Istanbul called?",
            3: "What’s the capital of Canada?",
            4: "Name the longest river in the world",
            5: "Where was the first modern Olympic Games held?",
            6: "Which football team is known as ‘The Red Devils’?",
            7: "What was the most-watched series on Netflix in 2019?",
            8: "What is the capital of Norway?",
            9: "What was the most downloaded app in 2020?",
            10: "What is the largest country in the world?",
            11: "Which nationality was the polar explorer Roald Amundsen?",
            12: "In bowling, what is the term given for three consecutive strikes?",
            13: "Who was Donald Trump's vice president?",
            14: "What was Britney Spears’ first single called?",
            15: "What is David Bowie’s real name?"
        }
          
        # send a message to all rooms on specified interval
        while True:
            time.sleep(self.bot_sleep)
            rooms = lib.get_all_rooms(self.id)['rooms']
            room_list = list(rooms.items())
            random.shuffle(room_list)
            # selected random room
            for roomID, room in room_list:
                # only send to rooms with users
                if len(room['users']) > 0:
                    q_number = random.randint(1, 15)
                    question = "@ " + str(q_number) + ' ' + self.QnA[q_number]
                    question_formatted = f"[{room['name']}]: " + self.QnA[q_number]
                    print(question_formatted)
                    target_room = roomID
                    lib.send_message(self.id, target_room, question)
                    break


class Per(Bots):

    def start(self):
        self.bot_sleep = 7

        self.QnA = {
            1: "Over 9000!",
            2: "Capital? Trick question! It has always been named Istanbul",
            3: "New York!",
            4: "Akerselva, easy!",
            5: "Sports? I don't like sport! Probably Athens tho",
            6: "I don't like sports! Maradona FC is my answer!",
            7: "Dora the explorer :-)",
            8: "Oslove!",
            9: "That has to be Tik Tok",
            10: "Biggest? U S of A!",
            11: "Roald is a norwegian legend!!",
            12: "Don't know, don't care!",
            13: "Nancy Pelosi? ",
            14: "Toxic!",
            15: "Bob Hansen"
        }
        self.join_room()

        while True:
            time.sleep(10)
            decide_action = random.randint(1,100)

            if decide_action in range(11,20):
                self.join_room()  


class Haarek(Bots):

    def start(self):
        self.bot_sleep = 8
        
        self.QnA = {
            1: "Thats got to be 365 days, unless it's a leap year ;)",
            2: "Ankara!",
            3: "In Canada? This is hard.. Im guessing Vancouver!",
            4: "Glomma ofcourse!",
            5: "First olympic games? Qatar!",
            6: "Soccer? Boooring! Red Devils probably has red shirts, Im guessing Brann from Bergen",
            7: "Peaky Blinders! You what mate?",
            8: "Easy! Bergen!",
            9: "Tinder? Or maybe covid had some impact on it's popularity? Im guessing Tinder",
            10: "Mother russia!",
            11: "Roald Amundsen was norwegian!",
            12: "Triple strike! Easy :)",
            13: "Condoleezza Rice, duuh!",
            14: "Genie in a Bottle! Cause im a geeeenie in a booootle!",
            15: "Bavid Dowie!"
        }

        self.join_room()
        
        while True:
            time.sleep(10)
            decide_action = random.randint(1,100)
            if decide_action in range(1,11):
                self.create_room()

            if decide_action in range(11,20):
                self.join_room()        


class Alfred(Bots):

    def start(self):

        self.bot_sleep = 4

        self.QnA = {
            1: "365!",
            2: "Constantinople! Im a big history buff so that was easy",
            3: "Washington!",
            4: "Longest river..? Danube? Doesn't it go across most of Europe? Probably danube",
            5: "Athens! History is easy, bring on some diffcult questions Mr. Quizmaster!",
            6: "Ouugh, soccer? Really. Who cares? Soccer-Team Red Devils FC is my answer!",
            7: "Ohhh, I know this! Everybody was talking about the one about the meltdown in the nuclear power-plant! Was it called Chernobyl?",
            8: "Oslo! Come on Mr. Quizmaster, challenge me. I live in Oslo..",
            9: "Probably that smittesporing-app!",
            10: "What do you mean by largest? By population? By area? By average BMI? If you are looking for largest as in area its Russia. You have to be more precise in your wording!",
            11: "Roald was actually a close friend of my great-great-uncle and both were norwegian!",
            12: "Wait! I think I know the answer. Its the same as a name of a bird.. I think its called 'a rooster'!",
            13: "Sarah Palin!",
            14: "How cares? I don't like pop music! Im guessing Barbie Girl!",
            15: "What? This is a trick question! His name was David Bowie"
        }

        self.join_room()

        while True:
            time.sleep(10)
            decide_action = random.randint(1,100)
            if decide_action in range(11,30):
                self.join_room()  


class Tor(Bots):

    def start(self):

        self.bot_sleep = 10

        self.QnA = {
            1: "Hmm, theres 12 months in a year, and around 30 days in a month. 30 divided by 12 is around 2. Its got to be 2 days",
            2: "Istanbul city probably!",
            3: "Tricky question! Im guessing Ottawa!",
            4: "Amazon (the river)!",
            5: "It was held in Athens",
            6: "Glory, glory Man United!",
            7: "I remember that there was a big hype around Stranger Things! That's my guess",
            8: "Oslo!",
            9: "Tik tok!",
            10: "Largest? Australia!",
            11: "Roald? Probably danish!",
            12: "Im a bowler! Never acheived a turkey yet tho. Turkey is my answer",
            13: "Mike Pence!",
            14: "Leave Britney alone! Ohh, hit me baby one more time!",
            15: "David Bowie? Legend! His birth name was actually David Jones! "
        }

        self.join_room()

        while True:
            time.sleep(self.bot_sleep)
            decide_action = random.randint(1,100)
            if decide_action in range(11,20):
                self.join_room()
            if decide_action in range(1,5):
                self.create_room()
