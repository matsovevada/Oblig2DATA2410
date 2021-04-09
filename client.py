import socket
import argparse
import os
import Bots
import time
import pickle
import threading

## CLIENT ## 

# parser, velg bot
# start bot

# connect to server

parser = argparse.ArgumentParser()
parser.add_argument("Bot", help="Available bots: Quizmaster, Per, Haarek, Alfred, Tor")
parser.add_argument("-n", "--notifications", action="store_true", help="To enable notifications")

args = parser.parse_args()

SERVER = 'localhost'
PORT = 5001
ADDR = (SERVER, PORT)
bot = args.Bot
active_bot = None


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
    print(f"{bot} is not a valid choice, please choose between the following bots: Per, Quiz-master")
    os._exit(1)


def receive():
    while True:
        data = client.recv(1024)
        if data:
            data_loaded = pickle.loads(data)
            alert = data_loaded['msg']
            print(alert)
            msg = active_bot.get_messages_in_room(data_loaded['roomID'])
            msg_split = msg.split(" ")
            #Room: 1 , 1: @ 11 Which nationality was the polar explorer Roald Amundsen?
            if msg_split[4] == "@":
                q_number = msg_split[5]

                #Formatting msg for terminal, removes "@" and q-number from string
                msg_split.pop(4)
                msg_split.pop(4)
                #['Room:', '4', ',', '1:', '13', 'was', 'Donald', "Trump's", 'vice', 'president?']
                msg_output = ""
                for word in msg_split:
                    msg_output += word + " "

                print(msg_output)
                active_bot.send_message(active_bot.QnA[int(q_number)])

            else:
                print(msg)


            

            


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
    except ConnectionRefusedError as e :
        print("[ERROR] Failed to connect to server: " + str(e))
        os._exit(1)


else: 
    thread = threading.Thread(target=active_bot.start)
    thread.start()
    while True:
        time.sleep(10)
        active_rooms = active_bot.bot_in_rooms()
        for room in active_rooms:
            active_bot.get_messages_in_room(room)

# lytt til notif
# reager på data -> bot 

