import socket

sock = socket.socket()

serverAddress = ('192.168.1.69', 9000)
sock.connect(serverAddress)

while True:
   command = raw_input("Insert here " + sock.recv(0x8000))
   sock.sendall(command)
sock.close()

