#client
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 7777
clientsocket.connect((host, port))

tm = clientsocket.recv(1024)

clientSocket.close()

print("the server time is ", tm.decode("ascii"))
