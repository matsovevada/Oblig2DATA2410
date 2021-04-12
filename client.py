import socket
import argparse
import os
import Bots
import time
import pickle
import threading
import library as lib

## CLIENT ## 


parser = argparse.ArgumentParser()
parser.add_argument("Bot", help="Available bots: Quizmaster, Per, Haarek, Alfred, Tor")
parser.add_argument("-n", "--notifications", action="store_true", help="To enable notifications")

args = parser.parse_args()

SERVER = 'localhost'
PORT = 5001
ADDR = (SERVER, PORT)
bot = args.Bot
active_bot = None

# Checks which bot the user chose when launching the client
if bot == 'Per':
    per = Bots.Per('Per')
    active_bot = per

elif bot == 'Quizmaster':
    quiz_master = Bots.Quiz_master('Quizmaster')
    active_bot = quiz_master

elif bot == 'Haarek':
    haarek = Bots.Haarek('Hårek')
    active_bot = haarek

elif bot == 'Alfred':
    alfred = Bots.Alfred('Alfred')
    active_bot = alfred

elif bot == 'Tor':
    tor = Bots.Tor('Tor')
    active_bot = tor

else:
    print(f"{bot} is not a valid choice, please choose between the following bots: Per, Quizmaster, Haarek, Tor, Alfred")
    os._exit(1)


# Formatting messages recieved from the quizmaster and rersponds to them
def respond(messages, roomID):
    if messages:
        for message in messages:
            msg_split = message.split(" ")
            if msg_split[2] == "@":
                q_number = msg_split[3]

                #Formatting msg for terminal, removes "@" and q-number from string
                msg_split.pop(2)
                msg_split.pop(2)
                msg_output = ""
                for word in msg_split:
                    msg_output += word + " "

                print(msg_output)
                active_bot.send_message(active_bot.QnA[int(q_number)], roomID)

            else:
                print(message)

# Recieves messages from the server
def receive():
    while True:
        data = client.recv(1024)
        if data:
            data_loaded = pickle.loads(data)
            #alert = data_loaded['msg']
            #print(alert)
            messages = active_bot.get_messages_in_room(data_loaded['roomID'], active_bot.id)
            respond(messages, data_loaded['roomID'] )


# Enables notifications if -n was input into the terminal
if args.notifications:
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[CONNECTING] Connecting to server...")
    try:
        client.connect(ADDR)
        bot_id = active_bot.register()
        client.send(str(bot_id).encode())
        thread = threading.Thread(target=active_bot.start)
        thread.start()
        receive()
    except ConnectionRefusedError as e:
        print("[ERROR] Failed to connect to server: " + str(e))
        os._exit(1)


# Disabled notifications
else: 
    thread = threading.Thread(target=active_bot.start)
    active_bot.register()
    thread.start()
    if active_bot.id != 1:     #Makes sure that Quizmaster does not respond the messages
        while True:
            time.sleep(3)
            active_rooms = active_bot.get_all_rooms()
            for room in active_rooms:
                unread_messages = active_bot.get_messages_in_room(room, active_bot.id)
                respond(unread_messages, room)
