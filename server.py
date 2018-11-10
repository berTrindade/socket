'''
Created on 4 de nov de 2018

@author: skywalker
'''

import socket

# socket.SOCK_STREAM == TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()

print ("The name of local machine: ", hostname)

sock.bind((hostname, 1234))

# Tells the socket library that we want it to queue up as many as 5 connect requests (the normal max) before refusing outside connections
sock.listen(5)

(client, address) = sock.accept()

print ("Got a connection from ", address," => Thanks...")

while 1:
    
    response_from_client = client.recv(1024)
    
    print ("FROM CLIENT ===> ", response_from_client)
    
    client.send(raw_input("TYPE A MESSAGE FOR CLIENT ==> "))
    
client.close()

sock.close()
    

