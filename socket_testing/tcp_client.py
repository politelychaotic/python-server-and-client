import socket, sys

HOST, PORT = "localhost", 50001
data = "Bob Dylan" #.join(sys.argv[0:])
buffer = 1024

#create a socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    #receive data from server
    received = str(sock.recv(buffer), "utf-8")

print("Sent: {}".format(data))
print("Received: {}".format(received))