
import socket

print('Hello,',"Dhruv")

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))

print("host name:",host," socket name:",socket)

print("Waiting for client to connect...")
s.listen()
while True:
    c,addr = s.accept()
    print('Got connection from', addr,'...')
    bytes = c.send(b'Thank you for connecting...')
    c.close()  # Close the connection