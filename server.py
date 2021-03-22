import socket

x = print('socket created')

s=socket.socket()
s.bind(('localhost',9999))
s.listen(3)
print('ready for connection')
while True:
    c,addr=s.accept()
    name = c.recv(1024).decode()
    print("connected with",addr,name)

    c.send(bytes("welcome to hell",'utf=8'))
    c.close()


