# Import socket library
from socket import *

# Import sys package if you want to terminate the program
import sys
def create_server_socket(port):
    # Prepare a sever socket
    # Fill in start
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', port))
    serverSocket.listen(1)
    # Fill in end
    print(f"The server is ready to receive on port: {port}")
    return serverSocket

def handle_request(connectionSocket):
        # Receive the HTTP request
        message = connectionSocket.recv(2048).decode()
        #print(message)
        # Prepare HTTP response header
        # Fill in start
        responseMessage = message.split()[2] + " 200 OK\r\n\r" + "Content-Type: text/html\r\n\r\n"
        # Fill in end

        # Get the requested file from the message
        filename = message.split()[1][1:]

        # Open the requested file and get the HTML body content
        # Fill in start
        try:
            file = open(filename, "r")
            responseMessage += file.read()
            file.close()
        except:
             responseMessage = message.split()[2] + " 404 Not Found\r\n\r" + "Content-Type: text/html\r\n\r\n" + "<html><head></head><body><h1>404 Not Found</h1></body></html>"
        # Fill in end

        # Send response message
        # Fill in start
        #print(responseMessage)
        connectionSocket.send(responseMessage.encode())
        # Fill in end

        # Close the socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

        # Terminate the program after sending the corresponding data
        # Comment it out if you want the server to be always ON
        sys.exit()

if __name__ == "__main__":
    port = 12000
    serverSocket = create_server_socket(port)
    while True:
        connectionSocket, addr = serverSocket.accept()
        handle_request(connectionSocket)
