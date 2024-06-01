import socket
from threading import Thread
import random
from math import sin, cos

from util import Angle, Vec
from consts import ACCELERATION, FRICTION, TERMINAL_VELOCITY, TURNING_ANGLE, WINDOW_DIMENSION, PORT


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", PORT))
sock.listen(5)

players = {}

def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class Player:
    def __init__(self, conn:socket.socket, addr, name, ID):
        self.conn = conn
        self.addr = addr
        self.name = name
        self.ID = ID
        self.vel = Vec(0, 0)
        self.acc = Vec(0, 0)
        self.accelerating = False
        self.position = Vec(0, 0)
        self.rotation = Angle(degree=0)

        self.coms_thread = Thread(target=self.event)
        self.coms_thread.start()

    def assign_acc(self, amplitude):
        self.acc.x = amplitude * sin(-self.rotation.radian)
        self.acc.y = amplitude * cos(-self.rotation.radian)

    def send(self, value):
        self.conn.send(str.encode(value))

    def event(self):
        print(f"{self.name} has connected")
        while True:
            data = self.conn.recv(2048)
            reply = data.decode()
            if not data:
                players.pop(self.ID)
                print(self.name + " left")
                break
            event, value = reply.split(":")
            if event == "keypress":
                if "w" in value:
                    self.accelerating = True
                    self.assign_acc(-ACCELERATION + FRICTION)
                if "a" in value:
                    vel = self.vel.mod()
                    self.rotation.offset(radian=-TURNING_ANGLE * vel)
                if "s" in value:
                    self.accelerating = True
                    self.assign_acc(ACCELERATION - FRICTION)
                if "d" in value:
                    vel = self.vel.mod()
                    self.rotation.offset(radian=TURNING_ANGLE * vel)
                self.send(f"x:{self.position.x}|y:{self.position.y}|angle:{self.rotation.degree}")

            if event == "get":
                if value == "self":
                    self.send(f"x:{self.position.x}|y:{self.position.y}|angle:{self.rotation.degree}")
                if value == "all":
                    ret_str = "players||"
                    for ID, player in players.items():
                        if ID != self.ID:
                            ret_str += f"id:{ID}|name:{player.name}|x:{player.position.x}|y:{player.position.y}|angle:{player.rotation.degree}||"
                    ret_str = ret_str[:-2]
                    self.send(ret_str)
                continue
            
            if not self.accelerating:
                self.acc.x = -sgn(self.vel.x)*min(FRICTION * 0.65, abs(self.vel.x))
                self.acc.y = -sgn(self.vel.y)*min(FRICTION * 0.65, abs(self.vel.y))

            self.vel = Vec.add(self.vel, self.acc)

            velocity = self.vel.mod()
            if velocity > TERMINAL_VELOCITY:
                self.vel.y = self.vel.y * TERMINAL_VELOCITY / velocity
                self.vel.x = self.vel.x * TERMINAL_VELOCITY / velocity
            
            self.position = Vec.add(self.position, self.vel)
            self.accelerating = False

def entry():
    while True:
        conn, addr = sock.accept()
        if len(players.keys()) >= 5:
            conn.close()
            continue
        name = conn.recv(1024).decode()
        ID = random.randint(1000, 9999)
        conn.send(str.encode(str(ID)))
        players[ID] = Player(conn, addr, name, ID)

entry()