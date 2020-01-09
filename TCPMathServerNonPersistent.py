import socket
import time
# LocalHost IP and Port chosen for Math
TCP_IP_ADDRESS = "127.0.0.1"
TCP_PORT_NO = 5000
#buffer size
BUFFER_SIZE= 1024
# declare serverSocket listening for TCP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Timeout setting
serverSock.settimeout(120)
# Bind the IP and Port to serverSock
serverSock.bind((TCP_IP_ADDRESS, TCP_PORT_NO))
serverSock.listen(1)
print("TCP NonPersistent Server is ready to receive inputs through port:%s"%(TCP_PORT_NO))
while True:
    try:
        connectionSocket,client_address = serverSock.accept()
        print("Connected to %s"%(str(client_address)))
        inputmessage = connectionSocket.recv(BUFFER_SIZE).decode()
        print("Message from Client (IP,PORT):%s): %s"%(str(client_address),inputmessage))
        try:
            # sleeping 30 seconds to make active rejections to connection in queue
            time.sleep(10)
            resultmessage = str(eval(inputmessage))
        except Exception as e:
            resultmessage = "Error in Input:%s"%(str(e))            
        print("Result to Send back:%s"%(resultmessage))
        connectionSocket.send(resultmessage.encode())
        print("Closing connection with %s"%(str(client_address)))
        connectionSocket.close()
    except Exception as e:
        print("Exiting Server with Exception: %s"%(str(e)))
        break        
serverSock.shutdown
serverSock.close()