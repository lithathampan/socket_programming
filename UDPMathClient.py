import socket

# LocalHost IP and Port chosen for Math
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
#buffer size
BUFFER_SIZE= 1024
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Timeout setting
clientSock.settimeout(30)

inputmessage = input("Enter your math expression (quit to stop):")

while inputmessage != 'quit':
    try:
        clientSock.sendto(inputmessage.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
        resultmessage, server_address = clientSock.recvfrom(BUFFER_SIZE)
        print("Result from Server:%s"%(resultmessage.decode()))
        inputmessage = input("Enter your math expression (quit to stop):")
    except Exception as e:
        print("Existing Client with Exception: %s"%(str(e)))
        break
print("Bye from Client")