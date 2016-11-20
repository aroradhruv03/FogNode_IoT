
# import socket
#
# print('Hello,',"Dhruv")
#
#
# socket_family = 'AF_INET';
# socket_type = 'SOCK_STREAM'; #SOCK_DGRAM
# protocol = 0;
#
# s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
#
# #host = socket.gethostname()
# host = '127.0.0.1'
# port = 12345
# s.bind((host,port))
#
# print("host name:",host," socket name:",socket)
#
# print("Waiting for client to connect...")
# s.listen(5)
# while True:
#     c,addr = s.accept()
#     print('Got connection from', addr,'...')
#     bytes = c.send(b'Thank you for connecting...')
#     c.close()  # Close the connection

import socketserver

from socket import *

sock = socket()
# use this before bind
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 12345

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
