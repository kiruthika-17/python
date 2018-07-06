import socket
UDP_IP_ADDRESS="10.1.24.138"
UDP_PORT_NO=6789
message=("surendar")
bytesToSend=str.encode(message)
clientSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSock.sendto(bytesToSend ,(UDP_IP_ADDRESS,UDP_PORT_NO))
