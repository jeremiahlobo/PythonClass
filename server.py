#Server
import socket
import time


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 5555
serversocket.bind((host,port))

serbersocket.listen(10)

while True:
    clientsocket,addr = serversocket.accept()

print("Connection from ", str(addr))
currentTime = time.ctime(time.time()) + "\r\n"
clientsocket.send(currentTime.encode("ascii"))
clientsocket.close()


#print(host)
#print(socket.gethostbyname_ex(host))
