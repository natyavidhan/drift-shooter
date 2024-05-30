import socket, sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = sys.argv[1]

client.connect(("localhost", 5050))
client.send(str.encode(name))

while True:
    text = input("> ")
    client.send(text.encode())