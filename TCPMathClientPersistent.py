import socket

# LocalHost IP and Port chosen for Math
TCP_IP_ADDRESS = "127.0.0.1"
TCP_PORT_NO = 5000
#buffer size
BUFFER_SIZE= 1024
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Timeout setting
clientSock.settimeout(60)
print("Connection to %s:%s"%(TCP_IP_ADDRESS,TCP_PORT_NO))
clientSock.connect((TCP_IP_ADDRESS,TCP_PORT_NO))
inputmessage = ''
while inputmessage != 'quit':
    try:
        inputmessage = input("Enter your math expression (quit to stop):")
        print("Sending to Server")
        clientSock.send(inputmessage.encode())
        resultmessage = clientSock.recv(BUFFER_SIZE).decode()
        print("Result from Server:%s"%(resultmessage))
    except Exception as e:
        print("Existing Client with Exception: %s"%(str(e)))
        break
clientSock.close()
print("Bye from Client")