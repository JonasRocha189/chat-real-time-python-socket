import socket

HOST = 'localhost'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = client.recv(1024)
if message == b"ROOM":
  client.send(b'Games')
  client.send(b'Jonas')