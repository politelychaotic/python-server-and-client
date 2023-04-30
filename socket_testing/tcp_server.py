import socketserver
import socket
import threading

SERVER_IP = "localhost"
SERVER_PORT = 50001

buffer = 1024

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    Request handler for the server.
    
    Instantiated once per connection to the server,
    must override the handle() method to implement 
    communication to the client.
    """

    def handle(self):
        #self.request is the TCP socket connected to the client
        self.data = self.request.recv(buffer).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        #send back same data, upper-case
        self.request.sendall(self.data.upper())

class MyStreamHandler(socketserver.StreamRequestHandler):
    """
    Same as the TCP handler, except this class makes use of streams
    (file-like objects that simplify communication by providing the
    standard file interface)
    """

    def handle(self):
        #self.rfile is a file-like object created by this handler
        self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        #self.wfile is a file-like object to send back data
        self.wfile.write(self.data.upper())

class MyRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            msg = self.request.recv()
            if msg == b"quit" or msg == "":
                break

            print(msg.decode())
            self.request.send(msg) # send message back to client

    def finish(self):
        self.request.close() # close socket


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer((SERVER_IP, SERVER_PORT), MyRequestHandler)

    server.serve_forever() #start the server