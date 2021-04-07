
import socket
import sys
import argparse
import os

## CLIENT ## 

# parser, velg bot
# start bot

# connect to server

SERVER = 'localhost'
PORT = 5001
ADDR = (SERVER, PORT)

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

# lytt til notif
# reager på data -> bot 

