##server side connection

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen()
print("waiting for client...")
while True:
    c,addr=s.accept()
    print("got connection from",addr)
    msg="networking socket"
    c.sendall(msg.encode('utf-8'))
    print(c.recv(1023).decode('utf-8'))
    c.close()


##client side connection

import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=12345
c.connect((host,port))
print("client started...")
print(c.recv(1023).decode('utf-8'))
