import socket
import time
import threading
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
print("TCP Persistent Server is ready to receive inputs through port:%s"%(TCP_PORT_NO))

def handle_connection(connectionSocket,client_address):
    while True:
            try:
                inputmessage = connectionSocket.recv(BUFFER_SIZE).decode()
                print("Message from Client (IP,PORT):%s): %s"%(str(client_address),inputmessage))
                try:
                    if inputmessage == "quit":
                        connectionSocket.send("Good bye".encode())
                        print ("Done with Client (IP,PORT):%s"%(str(client_address)))
                        connectionSocket.close()   
                        break
                    # sleeping 30 seconds to make active rejections to connection in queue
                    else:
                        time.sleep(10)
                        resultmessage = str(eval(inputmessage))
                except Exception as e:
                    resultmessage = "Error in Input:%s"%(str(e))            
                print("Result to Send back:%s"%(resultmessage))
                connectionSocket.send(resultmessage.encode())                
            except Exception as e:
                print("Exiting Connection with Exception: %s"%(str(e)))
                break
    print("Closing connection with %s"%(str(client_address)))
    connectionSocket.close() 
threadset=[]
connectionnumber = 0
while True:
    try:
        connectionnumber+=1
        connectionSocket,client_address = serverSock.accept()
        threadname = "Thread"+str(connectionnumber)
        print("New Thread:%s"%(threadname))
        print("Connected to %s"%(str(client_address)))
        client_handler = threading.Thread(name=threadname,target=handle_connection,
            args=[connectionSocket,client_address] 
            )
            # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
        client_handler.start()
        threadset.append(client_handler)
        #join any completed threads
        for thread in threadset:
            if thread.is_alive() is False :
                print("Stopping Thread:%s"%(thread.name)) 
                thread.join()
                threadset.remove(thread)
    except Exception as e:
        print("Exiting Server with Exception: %s"%(str(e)))
        break  
print("Waiting for established connections to close")
while len(threadset) > 0:
    for thread in threadset:
        if thread.is_alive() is False :
            print("Stopping Thread:%s"%(thread.name)) 
            thread.join()
            threadset.remove(thread)
print("Server shutting down")                   
serverSock.shutdown
serverSock.close()