# import socket               # Import socket module
#
# s = socket.socket()         # Create a socket object
# #host = socket.gethostname() # Get local machine name
# host = 'localhost'
# port = 12345                # Reserve a port for your service.
#
# s.connect((host, port))
# print('connecting to server...')
# print("host name:",host," socket name:",socket)
# print('Received: ',s.recv(1024))
# s.close                     # Close the socket when done
import socket
import sys

HOST, PORT = "123.123.123.123", 12345
print(sys.argv[0:]);
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")
finally:
    sock.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))