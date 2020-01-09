import socket

# LocalHost IP and Port chosen for Math
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
#buffer size
BUFFER_SIZE= 1024
# declare serverSocket listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Timeout setting
serverSock.settimeout(120)
# Bind the IP and Port to serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print("UDP Server is ready to receive inputs")
while True:
    try:
        inputmessage, client_address = serverSock.recvfrom(BUFFER_SIZE)
        print("Message from Client (IP,PORT):%s): %s"%(client_address,inputmessage))
        try:
            resultmessage = str(eval(inputmessage))
        except Exception as e:
            resultmessage = "Error in Input:%s"%(str(e))            
        print("Result to Send back:%s"%(resultmessage))
        serverSock.sendto(resultmessage.encode(), client_address)
    except Exception as e:
        print("Exiting Server with Exception: %s"%(str(e)))
        break
serverSock.shutdown
serverSock.close()