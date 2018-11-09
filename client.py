'''
Created on 4 de nov de 2018

@author: skywalker
'''

import socket

# socket.SOCK_STREAM == TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()

print ("The name of local machine: ", hostname)

sock.connect((hostname, 1234))

while 1:
    
    # sock.send(raw_input("TYPE A MESSAGE FOR SERVER ==> "))
    
    #sock.send("Hello")
    
    print ("TYPE A MESSAGE FOR SERVER ==> "),
    
    msg_for_server = raw_input()
    
    sock.send(msg_for_server + "\n")
        
    response_from_server = sock.recv(1024)
    
    print ("FROM SERVER ===> ", response_from_server)
    
sock.close()    
