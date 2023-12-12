import socket
import threading

HOST = 'localhost'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

rooms = {}

def broadcast(room, message):
  for i in rooms[room]:
    if isinstance(message, str):
      message = message.encode()
      i.send(message)
      # print(i)

def sendMessage(name, room, client):
  while True:
    message = client.recv(1024)
    message - f'{name}: {message.decode()} \n'
    broadcast(room, message)

while True:
  client, addr = server.accept()
  # print(client)

  client.send(b'ROOM')
  room = client.recv(1024).decode()
  name = client.recv(1024).decode()
  # print(room)

  if room not in rooms.keys():
    rooms[room] = []
  rooms[room].append(client)
  print(f'{name} has connected in the room {room}! INFO {addr}')
  broadcast(room, f'{name} entered the room \n')
  thread = threading.Thread(target = sendMessage, args=(name, room, client))
  thread.start()
