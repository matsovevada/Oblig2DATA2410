# Oblig2DATA2410

Submisson for Zakaria Karlsen Tawfiq s344072, Mats Ove Vada s340363, Peter Stjern Sund s344093

## Description

REST-API that allows for sending, retrieving and deleting users, rooms and messages in a chat. The
API is created using Python Flask. The API-calls are performed automatically by chat-bots in a
terminal. The chat-bots consist of a quizmaster which will send questions to chat rooms and bots that
will respond to the questions. The chat-bots will register themselves as users in the chat when started
and periodically create new rooms and join existing rooms.

## Installation

1. Download and extract the zip package
2. In a terminal navigate into the root directory
3. pip3 install -r requirements.txt
This will install the necessary modules from pip: flask, flask_restful
The program requires python3 and pip3 to be installed.

## Usage

### Starting server

In a terminal navigate into the root directory and use command

  python3 main.py
  
The server will by default start with push-notifications disabled.
When push-notifications are disabled the clients will fetch messages every 3 seconds.
To enable push-notifications start the server with the optional argument -n or –notifications: 

  python3 main.py -n
  
When push-notifications are enabled the clients will only fetch messages whenever a push notification
is sent from the server.

### Starting client

In a terminal navigate into the root directory and use command with a bot-name as argument. The
following names can be chosen: Quizmaster, Alfred, Haarek, Tor, Per.

 python3 client.py <bot-name>
 example: python3 client.py Quizmaster
 
The client will by default start with push-notifications disabled. To enable push-notifications start the
client with the optional argument -n or –notifications, for example: 

  python3 client.py Quizmaster -n
  
Both the client and the server must be run with the same settings for notifications, either enabled or
disabled.
Make sure to start a client with bot-name Quizmaster and at least another client with one of the other
bot-names to see interaction in the terminal.
