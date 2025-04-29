# from socket import *
# import time

# serverSocket = socket(AF_INET, SOCK_DGRAM)

# for i in range(1,11):
#     message = 'Ping ' + str(i) + ' ' + str(time.time())
#     serverSocket.sendto(message.encode(), ('localhost', 12000))
#     serverSocket.settimeout(1)
#     try:
#         modifiedMessage, serverAddress = serverSocket.recvfrom(1024)
#         print(modifiedMessage.decode())
#         print('RTT: ' + str(time.time() - float(modifiedMessage.decode().split(' ')[2])))
#     except timeout:
#         print('Request timed out')

from socket import *
import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(10):
    time1 = time.time()
    message = "Ping " + str(i+1) + " " + str(time1)

    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        time2 = time.time()
        rtt = time2-time1


        print(modifiedMessage.decode())

        print("rtt: " + str(rtt))
    except timeout:
        print("Request timed out")


clientSocket.close()