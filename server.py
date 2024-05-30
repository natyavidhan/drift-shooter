import socket
from threading import Thread
import random


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 5050))
sock.listen(5)

players = {}


class Player:
    def __init__(self, conn:socket.socket, addr, name):
        self.conn = conn
        self.addr = addr
        self.name = name
        self.x = 100
        self.y = 100

        self.thread = Thread(target=self.event)
        self.thread.start()

    def event(self):
        print(f"{self.name} has connected")
        while True:
            data = self.conn.recv(2048)
            reply = data.decode()
            if not data:
                break
            print(self.name, ": ", reply)

def entry():
    while True:
        conn, addr = sock.accept()
        if len(players.keys()) >= 5:
            conn.close()
            continue
        name = conn.recv(1024).decode()
        players[random.randint(1000, 9999)] = Player(conn, addr, name)

entry()