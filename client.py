import socket
import argparse
import os
import Bots

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


parser = argparse.ArgumentParser()
parser.add_argument("Bot", help="Available bots: Lars, Alice, Chuck, Bob or Dora")
parser.add_argument("-n", "--notifications", action="store_true", help="To enable notifications")

args = parser.parse_args()



def receive():
    while True:
        data = client.recv(1024).decode()
        print(data)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[CONNECTING] Connecting to server...")
try:
    client.connect(ADDR)
    receive()
except ConnectionRefusedError as e :
    print("[ERROR] Failed to connect to server: " + str(e))
    os._exit(1)

if bot == 'Per':
    per = Bots.Per('Per')
    per.start()

# lytt til notif
# reager på data -> bot 

