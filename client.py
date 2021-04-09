import socket
import argparse
import os
import Bots
import time
import pickle

## CLIENT ## 

# parser, velg bot
# start bot

# connect to server

parser = argparse.ArgumentParser()
parser.add_argument("Bot", help="Available bots: Per, Alice, Chuck, Bob or Dora")
parser.add_argument("-n", "--notifications", action="store_true", help="To enable notifications")

args = parser.parse_args()

SERVER = 'localhost'
PORT = 5001
ADDR = (SERVER, PORT)
bot = args.Bot
active_bot = None




parser = argparse.ArgumentParser()
parser.add_argument("Bot", help="Available bots: Lars, Alice, Chuck, Bob or Dora")
parser.add_argument("-n", "--notifications", action="store_true", help="To enable notifications")


args = parser.parse_args()

if bot == 'Per':
    per = Bots.Per('Per')
    active_bot = per



def receive():
    while True:
        data = client.recv(1024)
        if data:
            data_loaded = pickle.loads(data)
            print(data_loaded['msg'])
            #active_bot.get_messages_in_room(data['roomID'])

if args.notifications:
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[CONNECTING] Connecting to server...")
    try:
        client.connect(ADDR)
        active_bot.start()
        receive()
    except ConnectionRefusedError as e :
        print("[ERROR] Failed to connect to server: " + str(e))
        os._exit(1)


else: 
    active_bot.start()
    while True:
        time.sleep(10)
        active_rooms = active_bot.bot_in_rooms()
        for room in active_rooms:
            active_bot.get_messages_in_room(room)
        
        
        


# lytt til notif
# reager på data -> bot 

