import socket

#Server socket
PORT = 5001
SERVER = 'localhost'
ADDR = (SERVER, PORT)


if __name__ == '__main__':
    print("SERVER LISTENING...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    server.bind(ADDR)

    while True:
        server.listen()
        conn, addr = server.accept()
        print("Connected")


def notify(alert):
    if alert:
        msg = "Halloi"
        conn.send(msg.encode("utf-8"))