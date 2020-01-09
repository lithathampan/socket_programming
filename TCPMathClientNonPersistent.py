import socket

# LocalHost IP and Port chosen for Math
TCP_IP_ADDRESS = "127.0.0.1"
TCP_PORT_NO = 5000
#buffer size
BUFFER_SIZE= 1024

inputmessage = input("Enter your math expression (quit to stop):")

while inputmessage != 'quit':
    try:
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Timeout setting
        clientSock.settimeout(30)
        print("Connection to %s:%s"%(TCP_IP_ADDRESS,TCP_PORT_NO))
        clientSock.connect((TCP_IP_ADDRESS,TCP_PORT_NO))
        print("Sending to Server")
        clientSock.send(inputmessage.encode())
        resultmessage = clientSock.recv(BUFFER_SIZE).decode()
        print("Result from Server:%s"%(resultmessage))
        clientSock.close()
        inputmessage = input("Enter your math expression (quit to stop):")
    except Exception as e:
        print("Existing Client with Exception: %s"%(str(e)))
        break
print("Bye from Client")